---
title: System Prompt Optimization
category: guides
subcategory: system-prompt-optimization
tags:
- claude-code
- setup
- 新機能
date: '2026-07-26'
updated: '2026-07-26'
sources:
- url: https://qiita.com/Toriumi-desu/items/19cc2dd59f3dc03d4602
  title: 初学者が Opus5君出現により、Claude Codeの環境1日で全部やり直した話
  date: '2026-07-26'
---

# System Prompt Optimization

---

## 2026-07-26

### 初学者が Opus5君出現により、Claude Codeの環境1日で全部やり直した話

初学者が Anthropic の「システムプロンプト 80% 削減で性能低下なし」という公式発表を受けて、自身の Claude Code 環境（CLAUDE.md 100行、agents 10体、17,258B の description）を全面的に見直した体験記。CLAUDE.md を 31 行に、agents を 5 体に削減し、94% の削減を達成。削減後は claude doctor で検証し、実測値と見積もりのズレや、廃止された MCP サーバーの放置など環境の問題点も発見。安全系のルール（AWS の料金・セキュリティ制約）は permissions.deny との併用で残すべきか悩んだ過程も記録している。

- **ソース**: [Qiita claudecode](https://qiita.com/Toriumi-desu/items/19cc2dd59f3dc03d4602)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-26 | 自動生成 |
