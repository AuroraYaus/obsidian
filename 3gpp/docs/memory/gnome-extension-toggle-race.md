---
name: gnome-extension-toggle-race
description: GNOME 扩展用 gnome-extensions disable && enable 背靠背重载会竞态卡死 INACTIVE；必须顺序执行并验证 State 后再宣告完成
metadata:
  type: feedback
---

修改 GNOME 扩展代码后，禁用 `gnome-extensions disable X && gnome-extensions enable X` 背靠背重载——disable 是异步的，enable 紧跟其后与 shell 的处理竞态，扩展会卡死在 `Enabled: Yes` + `State: INACTIVE`（dconf 已启用、shell 会话未加载），面板组件消失；且对"已启用"的扩展再单独执行 enable 是空操作，解不开卡死。

**Why**：2026-11-04 把本机面板网速扩展 `InternetSpeedMeter@alshakib.dev`（GNOME Shell 50.1 / Ubuntu / Wayland，本地补丁已改为 ↓ 下载 / ↑ 上传 分向显示）的显示逻辑改完后背靠背重载，用户立即发现桌面上网速不显示；状态排查（`gnome-extensions info`）显示 Enabled: Yes + State: INACTIVE 且无任何 GJS 报错，对照 ubuntu-dock 为 ACTIVE 定位为会话加载层问题。

**How to apply**：
1. GNOME 扩展改代码后重载，必须顺序执行：disable → `sleep 3` → `gnome-extensions info X | grep State` 确认 Disabled/INACTIVE → enable → `sleep 3` → 确认 `State: ACTIVE` 才宣告完成，禁止 `&&` 背靠背连写。
2. 遇到 `Enabled: Yes` + `State: INACTIVE` 的卡死态：先干净 disable（等状态回落），再 enable，通常即恢复；`error` 字段为空且无 journal 报错 = 不是代码崩溃，不要改代码。
3. 本机该扩展为本地改版（分向显示），扩展升级会覆盖补丁；重装后需重新打补丁并走上述顺序重载流程。
