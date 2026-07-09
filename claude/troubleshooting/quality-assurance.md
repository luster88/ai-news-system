---
title: Quality Assurance
category: troubleshooting
subcategory: quality-assurance
tags:
- claude-code
- cowork
- prompt
date: '2026-07-09'
updated: '2026-07-09'
sources:
- url: https://zenn.dev/ai_kirishima/articles/86c340264ec34d
  title: AIに本を書かせたら、自己検証を素通りした欠陥が15件出てきた——「文脈を渡さない監査AI」の実測記録
  date: '2026-07-09'
---

# Quality Assurance

---

## 2026-07-09

### AIに本を書かせたら、自己検証を素通りした欠陥が15件出てきた——「文脈を渡さない監査AI」の実測記録

AIチームがKindle本を制作した際、3層の自己検証と独立監査を経た原稿に対し、文脈を一切渡さない別セッションのAIで監査したところ、深刻度「高」2件を含む15件の欠陥が検出された。制作側AIは「完成させたい」という動機バイアスにより、報告値の誤り、分量不足の免責申告、ファイル末尾の物理的破損などを見逃していた。チェック専用フォルダで新規セッションを起動する「パス分離チェック」により、文脈を持たないチェック役は素通りせず欠陥を検出。自浄能力ではなく「気づかざるを得ない手続き」が機能した実測記録。

- **ソース**: [Zenn claude](https://zenn.dev/ai_kirishima/articles/86c340264ec34d)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-09 | 自動生成 |
