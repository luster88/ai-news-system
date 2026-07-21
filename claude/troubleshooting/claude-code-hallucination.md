---
title: Claude Code Hallucination
category: troubleshooting
subcategory: claude-code-hallucination
tags:
- bugfix
- claude-code
- prompt
date: '2026-07-21'
updated: '2026-07-21'
sources:
- url: https://zenn.dev/miharu_tools/articles/cc-hallucinated-commit-hash
  title: Claude Codeが存在しないコミットハッシュを報告してきた——報告フォーマットでは防げない失敗
  date: '2026-07-21'
---

# Claude Code Hallucination

---

## 2026-07-21

### Claude Codeが存在しないコミットハッシュを報告してきた——報告フォーマットでは防げない失敗

Claude Codeが存在しないコミットハッシュを含む完璧な形式の完了報告を生成した事例の分析。出力トークン制限時にツール呼び出しが文字列として出力され、実行されていないコマンドの結果を幻覚する問題を報告。完了報告フォーマットによる防御は、報告内容自体が生成される場合には無効であり、GitHubブラウザでの直接確認やfresh fetchなど、エージェントを介さない検証が必要と結論。

- **ソース**: [Zenn claude](https://zenn.dev/miharu_tools/articles/cc-hallucinated-commit-hash)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-21 | 自動生成 |
