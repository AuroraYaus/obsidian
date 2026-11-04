---
name: gnome-extension-toggle-race
description: GNOME 扩展会话内 disable/enable 有两大坑：背靠背 toggle 竞态卡死 INACTIVE；改代码后会话内重载不生效（ESM 模块缓存）必须注销重登
metadata:
  type: feedback
---

修改 GNOME 扩展后会话内重载有两个坑：

1. `gnome-extensions disable X && gnome-extensions enable X` 背靠背执行会竞态——disable 是异步的，enable 紧随其后与 shell 的处理竞态，扩展卡死在 `Enabled: Yes` + `State: INACTIVE`（dconf 已启用、shell 会话未加载），面板组件消失；且对"已启用"的扩展再单独 enable 是空操作，解不开卡死。
2. 会话内 disable/enable **即使回到 ACTIVE，改过的代码也不生效**：GNOME 45+ 扩展是 ES 模块、按 gnome-shell 进程级缓存，disable/enable 只是用缓存里的旧模块重建类实例，不会重新读盘（2026-11-04 实测：shell 20:59 启动、21:07 改 extension.js，顺序重载后 State: ACTIVE 但面板仍是旧版 ⇅ 总和显示，用户指出"上下行还是没分开"）。**代码改动必须注销重新登录**（Wayland 无法会话内重启 shell；X11 可用 Alt+F2 + r）。

**Why**：2026-11-04 把本机面板网速扩展 `InternetSpeedMeter@alshakib.dev`（GNOME Shell 50.1 / Ubuntu / Wayland，本地补丁已改为 ↓ 下载 / ↑ 上传 分向显示）改完后踩了两个坑：背靠背重载卡死 INACTIVE（排查 `gnome-extensions info` + 对照 ubuntu-dock ACTIVE 定位），顺序重载后 ACTIVE 但用户发现显示未变，再排查进程启动时间（`ps -o lstart= -p $(pgrep -x gnome-shell)`）晚于文件 mtime，定位模块缓存机制。

**How to apply**：
1. GNOME 扩展重载必须顺序执行：disable → `sleep 3` → `gnome-extensions info X | grep State` 确认回落 → enable → `sleep 3` → 确认 `State: ACTIVE`；禁止 `&&` 背靠背连写。
2. **改代码后**：顺序重载只解决 INACTIVE 卡死；新代码要生效必须注销重登（或 X11 Alt+F2+r）。判断方法：shell 启动时间（`ps -o lstart= -p $(pgrep -x gnome-shell)`）早于文件修改时间 = 当前会话跑的旧代码。
3. 遇到 `Enabled: Yes` + `State: INACTIVE` 且 `error` 空、journal 无报错 = 竞态卡死而非代码崩溃，干净 disable 再 enable 即可恢复，不要改代码。
4. 本机该扩展为本地改版（分向显示），扩展升级会覆盖补丁；重装后需重新打补丁并注销重登生效。
