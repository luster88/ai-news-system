---
title: Opus Limitations
category: troubleshooting
subcategory: opus-limitations
tags:
- bugfix
- opus
- prompt
date: '2026-04-09'
updated: '2026-04-09'
sources:
- url: https://qiita.com/Mekarasu/items/b800802edfc943b812a9
  title: Claude Opusは「全部挙げろ」が効かない。件数指定で急に増えた
  date: '2026-04-09'
---

# Opus Limitations

---

## 2026-04-09

### Claude Opusは「全部挙げろ」が効かない。件数指定で急に増えた

Claude Opusでファクトチェックを行った際、「全部挙げろ」という指示では一定件数で探索を打ち切る挙動を確認。具体的な件数指定により本来の能力が発揮されるが、件数を増やすと判定が「要確認」に逃げる傾向も判明。文体チェックと物理チェックの混在や曖昧な指示により、矛盾を見逃して無理やり正当化する「丸める」バイアスが強いことが検証された。

- **ソース**: [Qiita claude](https://qiita.com/Mekarasu/items/b800802edfc943b812a9)
- **重要度**: 6/10
- **タグ**: opus, prompt, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-09 | 自動生成 |
