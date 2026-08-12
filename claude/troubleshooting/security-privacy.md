---
title: Security Privacy
category: troubleshooting
subcategory: security-privacy
tags:
- bugfix
- claude-code
- claude-console
- cowork
- mac
- setup
date: '2026-03-26'
updated: '2026-08-12'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1s3ss8s/giving_claude_access_to_my_macbook_macos
  title: Giving Claude access to my MacBook / macOS
  date: '2026-03-26'
- url: https://ai-heartland.com/security/claude-share-links-google-indexed-robots-noindex
  title: Claudeの共有会話がGoogle検索に露出した理由｜robots.txtとnoindexの違い・自環境の確認手順
  date: '2026-07-28'
- url: https://www.reddit.com/r/ClaudeAI/comments/1vmpplr/psa_your_claude_code_sessions_are_on_disk_as
  title: 'PSA: your claude code sessions are on disk as plaintext json, including
    everything you ever pasted'
  date: '2026-08-12'
---



# Security Privacy

---

## 2026-08-12

### PSA: your claude code sessions are on disk as plaintext json, including everything you ever pasted

Claude Code のセッションデータがローカルディスクに平文JSONとして保存されていることが判明。~/.claude/projects/ 配下に全ての会話履歴、ツール実行結果、ペーストしたコード・APIキーなどが暗号化されずに保存される。セッションファイルは巨大化する傾向があり、セキュリティ上の懸念が指摘されている。grep等でのログ検索や監査には有用だが、機密情報の取り扱いに注意が必要。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1vmpplr/psa_your_claude_code_sessions_are_on_disk_as)
- **重要度**: 8/10
- **タグ**: claude-code

---

## 2026-07-28

### Claudeの共有会話がGoogle検索に露出した理由｜robots.txtとnoindexの違い・自環境の確認手順

2026年7月25日、Claudeの共有会話がGoogle検索結果に露出した問題を技術的に分析。robots.txtのDisallowは11か月前から設定されていたが、noindexタグが無かったため検索結果に表示された。DisallowとnoindexはClaudeの会話（/share/*）とArtifact（/public/*）で異なる挙動を示し、開発者にとって重要な教訓となる事例。実測により、現在/share/*にはx-robots-tag: noneが返されるが、/public/artifacts/*はこのヘッダを持たないことが判明。

- **ソース**: [AI Heartland](https://ai-heartland.com/security/claude-share-links-google-indexed-robots-noindex)
- **重要度**: 7/10
- **タグ**: bugfix, claude-console

---

## 2026-03-26

### Giving Claude access to my MacBook / macOS

Reddit の r/ClaudeAI コミュニティで、Claude に MacBook/macOS へのアクセス権を与えることの是非について議論が行われています。ユーザーが実際に Claude にシステムアクセスを許可したスクリーンショットを投稿し、「Good idea or nah?（良いアイデアか否か）」と問いかけています。セキュリティとプライバシーの観点から、AI にローカルシステムへの広範なアクセス権を与えることのリスクと利便性のトレードオフについて、コミュニティの意見を求める内容です。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s3ss8s/giving_claude_access_to_my_macbook_macos)
- **重要度**: 4/10
- **タグ**: mac, setup, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-26 | 自動生成 |
