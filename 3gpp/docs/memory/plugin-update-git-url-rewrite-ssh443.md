---
name: plugin-update-git-url-rewrite-ssh443
description: claude plugin update/install 卡死在 GitHub https clone 时，用 GIT_CONFIG_COUNT 环境变量改写 URL 走 ssh.github.com:443
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f0bf5dca-7a56-450e-bad4-9bd297e6e460
  modified: 2026-08-22T04:44:10.723Z
---

2026-08-22 升级 superpowers 插件时发现：`claude plugin update` 内嵌的 `git clone https://github.com/...` 在大陆网络下会无限挂起（git-remote-https 卡死，120s 超时后被移到后台仍不结束）。

**Why:** Claude Code 插件系统用 https 直连 GitHub 拉取插件源（marketplace.json 里的 `source.url`），不走用户 ~/.ssh/config 的 ssh.github.com:443 通道；GFW 下 https 直连会挂起而非快速失败。

**How to apply:** 杀掉卡死任务后，用 git URL 改写环境变量重跑（对 CLI 派生的所有 git 子进程生效）：

```bash
GIT_CONFIG_COUNT=1 \
GIT_CONFIG_KEY_0='url.git@github.com:.insteadOf' \
GIT_CONFIG_VALUE_0='https://github.com/' \
claude plugin update <plugin>@<marketplace>
```

`git@github.com:` 会自动命中 ~/.ssh/config 的 Host github.com → ssh.github.com:443。同理适用于 `claude plugin install`、marketplace 内 git 仓库的 fetch（`git fetch git@github.com:owner/repo.git` 直连 443，几秒完成）。

关联：[[dual-push-gitee-github]]（443 通道背景）、[[claude-settings-json-do-not-modify]]（插件操作只用 claude plugin CLI，不手改 settings.json）。
