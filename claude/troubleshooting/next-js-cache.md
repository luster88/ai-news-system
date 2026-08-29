---
title: Next Js Cache
category: troubleshooting
subcategory: next-js-cache
tags:
- bugfix
- claude-code
- setup
date: '2026-08-29'
updated: '2026-08-29'
sources:
- url: https://qiita.com/ennagara128/items/5a3ef4c616a7d5a77839
  title: Server Actionでデータを追加したのに、一覧に反映されない理由 — revalidatePathで直す
  date: '2026-08-29'
---

# Next Js Cache

---

## 2026-08-29

### Server Actionでデータを追加したのに、一覧に反映されない理由 — revalidatePathで直す

Next.jsのApp RouterとServer Actionでデータを追加後、一覧画面に反映されない問題と解決法を解説。データベースへの保存は成功していても、Next.jsのキャッシュが自動更新されないため、revalidatePath()を呼び出して明示的にキャッシュを無効化する必要がある。Claude Codeが生成するCRUDコードでは、このキャッシュ更新処理が抜けていることがあるため、実装後の確認が重要。

- **ソース**: [Qiita claudecode](https://qiita.com/ennagara128/items/5a3ef4c616a7d5a77839)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-29 | 自動生成 |
