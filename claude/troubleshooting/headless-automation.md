---
title: Headless Automation
category: troubleshooting
subcategory: headless-automation
tags:
- claude-code
- mac
- setup
date: '2026-06-23'
updated: '2026-06-23'
sources:
- url: https://qiita.com/claute_colo/items/120a92094cdcfacf7f78
  title: 夜間のlaunchd Claude Codeジョブがpermissionで毎晩ブロックされた — settings.local.jsonが効かない原因は
    cwd=/、--allowedTools で解決した
  date: '2026-06-23'
---

# Headless Automation

---

## 2026-06-23

### 夜間のlaunchd Claude Codeジョブがpermissionで毎晩ブロックされた — settings.local.jsonが効かない原因は cwd=/、--allowedTools で解決した

macOSのlaunchdから夜間実行するClaude Codeジョブが、permission不足で毎晩失敗していた問題の解決記録。settings.local.jsonを配置していたが、launchdの作業ディレクトリが/（ルート）のため読み込まれず、--allowedToolsオプションで起動時に明示的に許可することで解決。acceptEditsモードはEdit/Writeのみ自動承認でBash/WebSearchは止まること、Bashの複合コマンド（&&）は分割評価されることも判明。

- **ソース**: [Qiita claudecode](https://qiita.com/claute_colo/items/120a92094cdcfacf7f78)
- **重要度**: 6/10
- **タグ**: claude-code, setup, mac

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-23 | 自動生成 |
