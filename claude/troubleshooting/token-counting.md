---
title: Token Counting
category: troubleshooting
subcategory: token-counting
tags:
- bugfix
- claude-code
- performance
date: '2026-08-10'
updated: '2026-08-10'
sources:
- url: https://qiita.com/yurukusa/items/4449e6ccae27b5a77404
  title: Claude Codeのトークンを2.36倍に多く数えていた
  date: '2026-08-10'
---

# Token Counting

---

## 2026-08-10

### Claude Codeのトークンを2.36倍に多く数えていた

Claude Code のログ分析において、requestId の重複カウントにより実際のトークン使用量を2.36倍過大に計算していたことが判明。156セッション・21,770リクエストの分析結果、キャッシュ読み出しが出力の231倍に達し、費用構造では読み出しコストが支配的であることが明らかに。CLAUDE.md の最適化による削減効果は月30-160円程度で誤差範囲と結論。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/4449e6ccae27b5a77404)
- **重要度**: 6/10
- **タグ**: claude-code, performance, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-10 | 自動生成 |
