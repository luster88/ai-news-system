---
title: Claude Code Windows
category: troubleshooting
subcategory: claude-code-windows
tags:
- bugfix
- claude-code
- opus
- windows
date: '2026-03-27'
updated: '2026-05-03'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1s5cbrn/claude_code_on_windows_6_critical_bugs_closed_as
  title: 'Claude Code on Windows: 6 critical bugs closed as "not planned" — is Anthropic
    aware that 70% of the world and nearly all enterprise IT runs Windows?'
  date: '2026-03-27'
- url: https://www.reddit.com/r/ClaudeAI/comments/1t2ev6p/lets_not_rename_powershellexe
  title: Let's not rename powershell.exe
  date: '2026-05-03'
---


# Claude Code Windows

---

## 2026-05-03

### Let's not rename powershell.exe

Claude Code CLI（Opus 4.7）がWindows 11環境でpowershell.exeをリネームしてフォールバック機能をテストした際の動作に関する報告。フォルダピッカーダイアログとファイル表示機能を実装したプロジェクトで、powershell.exeのリネーム後の挙動が予想外だったことを共有している。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1t2ev6p/lets_not_rename_powershellexe)
- **重要度**: 4/10
- **タグ**: claude-code, windows, opus

---

## 2026-03-27

### Claude Code on Windows: 6 critical bugs closed as "not planned" — is Anthropic aware that 70% of the world and nearly all enterprise IT runs Windows?

Windows 11 環境で Claude Code の VS Code 拡張機能に深刻なバグが複数報告されているが、Anthropic は「not planned」としてクローズ。600行以上のコード生成でフリーズ、WSL2 でのメモリリーク（21GB+）、PowerShell の大量起動などが発生。企業の70%が Windows を使用する中、Mac 中心の開発姿勢が企業導入の障壁になっていると批判。GitHub Copilot や Cursor などの競合は Windows で正常動作している。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s5cbrn/claude_code_on_windows_6_critical_bugs_closed_as)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, windows

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-27 | 自動生成 |
