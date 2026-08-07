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

相关：[[lesson-error-fix-must-solidify]]
