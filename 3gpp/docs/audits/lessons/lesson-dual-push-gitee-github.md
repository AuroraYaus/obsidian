# dual-push-gitee-github

> 推送必须同时到 Gitee 和 GitHub——origin 已配双 pushurl（git push origin master 一次双推），大陆直连 GitHub 慢时用 ssh.github.com:443

2026-08-07 用户要求："下次推送记得两个网站都要推送"（Gitee + GitHub）。

**已配置（git 层强制，不依赖记忆）**：`git remote set-url --add origin git@github.com:aurorayaus/obsidian.git`——`origin` 现在有两个 push URL（Gitee HTTPS + GitHub SSH），`git push origin master` 一次推两个网站（验证输出两条 Everything up-to-date）。

**网络经验**：
- 大陆直连 GitHub 全量推送不可行（实测 TCP 停滞，Send-Q 330KB 卡死）
- `ssh.github.com:443` 通道可用（~/.ssh/config 已配 Host github.com → HostName ssh.github.com Port 443）
- 大仓库（618MB，含 3GPP 协议抽取 document.xml 大对象）首次同步用 **GitHub Import 服务器中转**（https://github.com/new/import 填 Gitee URL），后续增量推送走 443 秒级完成

**How to apply**：
1. 推送统一 `git push origin master`（自动双推）；单独推用 `git push github master` / `git push origin master`（fetch 仍只从 Gitee）
2. 新建仓库/换机器时：配置 origin 双 pushurl + ssh config（github.com → ssh.github.com:443）+ 公钥
3. 全量首次同步走 GitHub Import，不要本地直推大仓库

## 补记：换机恢复双推的完整命令链（2026-09-03）

2026-09-03 新工作区拷贝丢失双推配置（origin 仅剩 Gitee HTTPS；本机无 SSH 密钥、ssh config 无 443 映射、known_hosts 无 `[ssh.github.com]:443` 条目），且全局存在 `url.https://github.com/.insteadof git@github.com:` 会把 scp 式 SSH URL 改写成 HTTPS。恢复过程暴露三个坑：

1. `git remote set-url --add --push origin <url>` 在**尚无 pushurl 时只写入新值**——原隐式 push（fetch URL 即 Gitee）被顶掉；多值 pushurl 存在时 `set-url --push` 直接报 "could not set"——必须 `git config --unset-all remote.origin.pushurl` 后逐条 `--add` 重建。
2. insteadOf 改写陷阱：配置 `git@github.com:...` 会被全局 insteadOf 变 HTTPS——SSH 推送必须用显式 `ssh://git@ssh.github.com:443/AuroraYaus/obsidian.git` 形式（或先确认/删除 insteadOf 规则）。
3. 主机密钥：ssh.github.com:443 与 github.com:22 同密钥，可用已信任的 known_hosts 条目交叉验证后固定（`ssh-keyscan -p 443 ssh.github.com` → 比对 ed25519 → printf 追加 `[ssh.github.com]:443` 行）。

**标准恢复命令链**（新机器/新拷贝）：

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "<user>"   # 公钥登记 GitHub Settings→SSH keys
printf '\nHost github.com\n  HostName ssh.github.com\n  Port 443\n  User git\n' >> ~/.ssh/config
ssh-keyscan -p 443 ssh.github.com >> ~/.ssh/known_hosts          # 与已信任 github.com 密钥比对后固定
git config --unset-all remote.origin.pushurl
git config --add remote.origin.pushurl https://gitee.com/aurorayaus/obsidian.git
git config --add remote.origin.pushurl ssh://git@ssh.github.com:443/AuroraYaus/obsidian.git
```

GitHub 仓库规范名 `AuroraYaus/obsidian`（小写旧名 redirect 可用）；Gitee 2FA 账号推送凭据必须是私人令牌（Windows 凭据管理器 `git:https://gitee.com`，密码字段填令牌，令牌不得贴聊天）。

## 相关教训

- [[lesson-error-fix-must-solidify]]
