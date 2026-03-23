# Claude エコシステム情報サイト — 調査・計画書

作成日: 2026-03-23
ステータス: 計画段階（実装前）

---

## 1. Project Understanding

### 既存プロジェクトの構造（README.md / HANDOFF.md に基づく）

このリポジトリ `ai-news-system` は「AI ニュースの自動収集・要約・静的サイト公開パイプライン」である。

**現在のアーキテクチャ:**

```
[データ取得]  feeds.yaml(22ソース/5リージョン) → collect.py(RSS/スクレイピング)
    ↓
[フィルタ]   seen_urls.py(重複排除・ペナルティ)
    ↓
[本文取得]   fetch_body.py(HTTP + キャッシュ)
    ↓
[AI要約]     summarize.py(Claude API → 日本語要約・スコア・タグ)
    ↓
[生成]       render_markdown.py → news/YYYY/MM/YYYY-MM-DD.md
    ↓
[サイト構築] build_site.py → _site/(HTML + CSS + 検索 + タグ)
    ↓
[デプロイ]   GitHub Actions → GitHub Pages
```

**build_site.py の構造（統合に重要）:**
- `page_shell()` — 全ページ共通のHTML シェル（ヘッダー・ナビ・フッター・検索）
- ナビゲーション: トップ / モデル一覧 / 検索 / タグ一覧 の4リンク
- `build_index_pages()` — 日報一覧（ページネーション付き）
- `build_article_pages()` — 個別日報ページ
- `build_tag_pages()` — タグ別一覧 + タグ一覧ページ
- `build_search_index()` + `build_search_page()` — JSON 検索インデックス + 検索ページ
- `build_model_page()` — モデルまとめ（latest + history）
- `main()` のエントリポイントでこれらを順次実行

**GitHub Actions パターン:**
- `daily-news.yml`: 毎日 JST 01:05 自動実行 → `scripts.main` → git add news/ index.md → コミット → `scripts.build_site` → Pages デプロイ
- `model-report.yml`: 手動実行（workflow_dispatch）
- `deploy-pages.yml`: 手動再デプロイ

**既存の重複排除の仕組み:**
- `seen_urls.json` で URL 単位の既出管理（90日保持）
- `compute_source_penalties()` で同一ソースの連続重複にペナルティ

### 今回の要件の本質

既存の「AI ニュース日報」パイプラインと**並行して**、**Claude エコシステム（Claude / Claude Code / Claude Console / 関連ツール）に特化した情報を毎日自動収集し、カテゴリ別に整理して GitHub Pages で公開する新しいコンテンツ系統**を追加する。

既存の日報パイプラインとの重要な違い:
- **日報形式（日付ごとの1ファイル）ではなく、カテゴリ/トピック別に整理されたページ群**
- **重複排除は URL 単位だけでなく、内容レベルでの重複も排除**
- **蓄積型**: 新情報を既存カテゴリに追記していく運用
- **将来的に MkDocs / Obsidian のような検索・リンク機能**

---

## 2. Assumptions / Constraints

### 前提

- Claude エコシステムの最新情報を毎日ウェブから収集する（手動 + 将来的に自動化）
- 収集した情報は Markdown 形式で蓄積
- GitHub Pages で公開する（既存の AI News サイトと統合 or 隣接）
- カテゴリ/セクション別に理路整然とした構成にする
- 重複情報は記録しない
- 将来的に MkDocs / Obsidian 的な検索・相互リンク機能が必要

### 制約

- **既存パイプライン（日報・モデルまとめ）を壊さない**
- `build_site.py` は既に 1062 行あり、複雑。大幅改修のリスクを最小化する
- GitHub Actions の `daily-news.yml` は安定運用中。新しいワークフローは別ファイルで追加が望ましい
- `_site/` は gitignore 済み（ビルド時に生成）。新コンテンツもこの方式に従う
- API コスト: 既存パイプラインが Claude API を使用中。新パイプラインのコスト増を考慮
- `.env` の `ANTHROPIC_API_KEY` は既存。新たなキー追加は不要（同じ API を使える）

### 不明点・要確認事項

| # | 項目 | 仮説 |
|---|------|------|
| 1 | **情報収集の自動化レベル** | Phase 1 は手動収集 + Markdown 作成、Phase 2 で RSS/スクレイピング自動化 |
| 2 | **既存 AI News サイトとの統合度** | 同一サイト内に `/claude/` セクションとして統合（同一ドメイン・同一ナビ） |
| 3 | **収集対象の具体的なソース** | Anthropic 公式ブログ、Claude Docs、GitHub Releases、X/Reddit、テックブログ等 |
| 4 | **更新頻度** | 日次で新情報をチェック。変更があれば追記 |
| 5 | **情報の粒度** | リリースノート級の大きな変更から Tips 級の小さな知見まで |
| 6 | **言語** | 日本語でまとめる（ソースは英語/日本語混在） |
| 7 | **MkDocs 移行タイミング** | Phase 3 以降。まずは既存 build_site.py の拡張で対応 |

---

## 3. 情報設計 — カテゴリ体系

Claude エコシステムの情報を以下のカテゴリで整理する（仮説）:

```
claude/
├── releases/          リリースノート・アップデート情報
│   ├── claude-model/    Claude モデル（Opus, Sonnet, Haiku）のアップデート
│   ├── claude-code/     Claude Code のリリース・機能追加
│   ├── claude-console/  Claude Console の変更
│   └── api/             API の変更・新機能
│
├── guides/            使い方ガイド・セットアップ
│   ├── setup/           セットアップ手順
│   ├── workflow/        ワークフロー・活用法
│   └── best-practices/  ベストプラクティス
│
├── troubleshooting/   トラブルシューティング
│   ├── errors/          よくあるエラーと対処法
│   └── environment/     環境別の問題（Windows/Mac/Linux）
│
├── tools/             関連ツール
│   ├── cursor/          Cursor との連携
│   ├── cowork/          Cowork の使い方
│   ├── mcp/             MCP サーバー関連
│   └── comparison/      ツール比較
│
├── prompts/           プロンプト関連
│   ├── templates/       プロンプトテンプレート
│   └── techniques/      プロンプトエンジニアリング技法
│
└── ecosystem/         エコシステム全般
    ├── pricing/         料金・プラン情報
    ├── community/       コミュニティ動向
    └── competitors/     競合比較・ポジショニング
```

---

## 4. Task Breakdown

### Epic 1: 情報設計・方針確定

| Task | Subtask | 説明 |
|------|---------|------|
| 1.1 カテゴリ体系の確定 | 1.1.1 カテゴリ一覧レビュー | 上記案をベースに最終確定 |
| | 1.1.2 タグ体系の設計 | frontmatter tags のホワイトリスト設計 |
| | 1.1.3 命名規則の策定 | ファイル名: kebab-case、カテゴリ名、URL パス |
| 1.2 重複排除の方針 | 1.2.1 URL ベース重複排除 | 既存 seen_urls.py のパターンを流用 |
| | 1.2.2 内容ベース重複排除 | 同じトピックの更新情報は既存記事に追記 vs 新記事 |
| 1.3 情報収集ソースの特定 | 1.3.1 RSS/サイト候補リスト | Anthropic Blog, GitHub Releases, Docs changelog 等 |
| | 1.3.2 ソース別の取得方式 | RSS / スクレイピング / API / 手動 |

### Epic 2: ディレクトリ・ファイル設計

| Task | Subtask | 説明 |
|------|---------|------|
| 2.1 ソースデータの配置 | 2.1.1 `claude/` ディレクトリ新設 | プロジェクトルートに `claude/` を追加 |
| | 2.1.2 カテゴリ別サブディレクトリ | `claude/releases/`, `claude/guides/` 等 |
| 2.2 Markdown テンプレート | 2.2.1 記事テンプレート設計 | frontmatter: title/category/tags/date/updated/sources |
| | 2.2.2 カテゴリインデックス | 各カテゴリの README.md（目次・説明） |
| 2.3 データ管理 | 2.3.1 `data/claude_feeds.yaml` | Claude 関連ソース定義 |
| | 2.3.2 `data/claude_seen_urls.json` | 重複排除用 URL 履歴 |

### Epic 3: 収集パイプライン構築

| Task | Subtask | 説明 |
|------|---------|------|
| 3.1 ソース定義 | 3.1.1 `data/claude_feeds.yaml` 作成 | Claude 関連の情報ソースを定義 |
| 3.2 収集スクリプト | 3.2.1 `scripts/claude_collect.py` | RSS/スクレイピングで Claude 関連情報を収集 |
| | 3.2.2 重複排除ロジック | URL + タイトル類似度で重複判定 |
| 3.3 要約・分類スクリプト | 3.3.1 `scripts/claude_summarize.py` | Claude API で日本語要約 + カテゴリ自動分類 + タグ付与 |
| 3.4 Markdown 生成 | 3.4.1 `scripts/claude_render.py` | カテゴリ別 Markdown ファイルへの追記/新規生成 |
| 3.5 統括スクリプト | 3.5.1 `scripts/claude_main.py` | 収集→要約→分類→生成を一括実行 |

### Epic 4: サイト生成の拡張

| Task | Subtask | 説明 |
|------|---------|------|
| 4.1 build_site.py 拡張 | 4.1.1 `build_claude_pages()` 関数追加 | `claude/` の Markdown → `_site/claude/` の HTML |
| | 4.1.2 カテゴリ別インデックスページ | カテゴリ一覧 + 記事一覧ページ |
| | 4.1.3 個別記事ページ | 各記事の詳細ページ |
| 4.2 ナビゲーション統合 | 4.2.1 `page_shell()` のナビに追加 | 「Claude Info」リンクをヘッダーに追加 |
| | 4.2.2 Claude セクション専用ナビ | カテゴリサイドバー or タブ |
| 4.3 検索統合 | 4.3.1 検索インデックスに Claude 記事を追加 | `build_search_index()` を拡張 |
| 4.4 タグ統合 | 4.4.1 Claude 記事のタグをタグページに統合 | `build_tag_pages()` を拡張 |

### Epic 5: 自動化（GitHub Actions）

| Task | Subtask | 説明 |
|------|---------|------|
| 5.1 ワークフロー作成 | 5.1.1 `.github/workflows/claude-info.yml` | 日次 or 手動実行で Claude 情報を収集 |
| | 5.1.2 コミット対象の定義 | `claude/`, `data/claude_seen_urls.json` |
| 5.2 既存ワークフローとの連携 | 5.2.1 daily-news.yml でサイト再ビルド | Claude 記事もサイトに含める |
| | 5.2.2 実行順序の設計 | claude-info → daily-news の順序 or 統合 |

### Epic 6: 将来の検索・リンク機能（MkDocs 移行）

| Task | Subtask | 説明 |
|------|---------|------|
| 6.1 移行計画策定 | 6.1.1 MkDocs vs Obsidian Publish vs 自前 | 比較検討 |
| | 6.1.2 既存サイトとの共存方式 | news 系は build_site.py、claude 系は MkDocs 等 |
| 6.2 MkDocs 導入（Phase 3） | 6.2.1 mkdocs.yml 設定 | テーマ・ナビ・検索・プラグイン |
| | 6.2.2 既存 Markdown との互換性確保 | frontmatter の統一 |

---

## 5. Options Comparison

### 案A: `claude/` ディレクトリ + build_site.py 拡張

**概要**: プロジェクトルートに `claude/` を新設し、build_site.py に `build_claude_pages()` を追加して `_site/claude/` に HTML を生成。

```
ai-news-system/
├── news/          ← 既存（日報）
├── models/        ← 既存（モデルまとめ）
├── claude/        ← 新規（Claude エコシステム情報）
│   ├── releases/
│   ├── guides/
│   ├── tools/
│   └── ...
├── scripts/
│   ├── main.py              ← 既存
│   ├── claude_main.py       ← 新規
│   ├── claude_collect.py    ← 新規
│   ├── claude_summarize.py  ← 新規
│   └── claude_render.py     ← 新規
└── data/
    ├── feeds.yaml           ← 既存
    ├── claude_feeds.yaml    ← 新規
    └── claude_seen_urls.json ← 新規
```

| 項目 | 評価 |
|------|------|
| メリット | 既存構造（news/, models/）と同じレベルの並列構造。build_site.py の拡張パターンは models/ で実績あり。既存のサイトテーマ・ナビ・検索と統一感がある |
| デメリット | build_site.py がさらに肥大化する。カテゴリ別ページ生成は日報形式と異なるロジックが必要 |
| リポジトリ相性 | ◎ news/ と models/ の並列として自然 |
| MkDocs 移行性 | ○ claude/ ディレクトリがそのまま MkDocs のドキュメントルートになる |
| おすすめ度 | ★★★★★ |

### 案B: `docs/claude/` 配下に配置 + build_site.py 拡張

**概要**: docs/ 内に配置し、内部ドキュメントの延長として扱う。

| 項目 | 評価 |
|------|------|
| メリット | HANDOFF.md と同じ docs/ 内 |
| デメリット | docs/ は「プロジェクトのドキュメント」の場所であり、「公開コンテンツのソース」としては不自然。news/ や models/ と並列にならない |
| リポジトリ相性 | △ 公開コンテンツとしては docs/ は不適切 |
| おすすめ度 | ★★☆☆☆ |

### 案C: 最初から MkDocs で別ビルド

**概要**: Claude セクションだけ MkDocs で構築し、`_site/claude/` にビルド結果を統合。

| 項目 | 評価 |
|------|------|
| メリット | 検索・ナビ・相互リンクが最初から充実。将来の移行が不要 |
| デメリット | 導入コストが高い。既存サイトとのテーマ統一が困難。ビルドパイプラインが複雑化（build_site.py + mkdocs build の二重ビルド）。GitHub Actions の改修が大きい |
| リポジトリ相性 | △ 既存の自前ビルドとの混在が複雑 |
| おすすめ度 | ★★★☆☆（Phase 3 としては ◎） |

### 案D: 既存 feeds.yaml にソースを追加して日報に統合

**概要**: Claude 関連ソースを既存パイプラインに追加し、AI ニュース日報の一部として扱う。

| 項目 | 評価 |
|------|------|
| メリット | 実装コスト最小。既存パイプラインをそのまま活用 |
| デメリット | **要件を満たさない**。日付ベースの日報にカテゴリ別整理はできない。蓄積型の情報管理ができない。Claude 固有の深い情報整理に不向き |
| おすすめ度 | ★☆☆☆☆ |

### 比較まとめ

| 観点 | 案A (claude/) | 案B (docs/) | 案C (MkDocs) | 案D (日報統合) |
|------|:------------:|:-----------:|:------------:|:-------------:|
| 要件充足度 | ◎ | ○ | ◎ | × |
| 既存構成との整合 | ◎ | △ | △ | ◎ |
| 導入コスト | 中 | 低 | 高 | 最低 |
| カテゴリ別整理 | ◎ | ○ | ◎ | × |
| 重複排除 | ◎ | ○ | ○ | △ |
| サイト統合 | ◎ | △ | △ | ◎ |
| MkDocs 移行性 | ◎ | ○ | 不要 | × |
| 将来の検索性 | ○→◎ | ○ | ◎ | △ |

---

## 6. Recommended Plan

### 推奨: 案A（`claude/` ディレクトリ + build_site.py 拡張）を段階的に実施

**選定理由:**

1. **既存構造との自然な並列**: `news/`（日報）、`models/`（モデルまとめ）、`claude/`（Claude エコシステム）という3本柱の構造が最も直感的
2. **models/ の実装パターンを踏襲**: build_site.py に `build_model_page()` を追加した実績と同じパターンで `build_claude_pages()` を追加できる
3. **段階的に構築可能**: Phase 1（手動 + 最小構成）→ Phase 2（自動収集）→ Phase 3（MkDocs 移行）と段階的に拡張可能
4. **MkDocs 移行が自然**: `claude/` ディレクトリがそのまま MkDocs の docs ルートになる。Markdown の frontmatter を統一しておけば移行コストが低い

### 実施フェーズ

```
Phase 1: 最小構成 — 手動運用 + サイト公開（1-2日）
  ├── claude/ ディレクトリ + 初期カテゴリ作成
  ├── Markdown テンプレート + frontmatter 仕様確定
  ├── build_site.py に build_claude_pages() 追加
  ├── ナビゲーションに「Claude Info」追加
  ├── 初期コンテンツ 3-5 記事を手動作成
  └── README.md / HANDOFF.md 更新

Phase 2: 自動収集パイプライン（3-5日）
  ├── data/claude_feeds.yaml 作成（ソース定義）
  ├── scripts/claude_collect.py（収集）
  ├── scripts/claude_summarize.py（要約・分類）
  ├── scripts/claude_render.py（Markdown 生成）
  ├── scripts/claude_main.py（統括）
  ├── data/claude_seen_urls.json（重複排除）
  ├── .github/workflows/claude-info.yml（自動実行）
  └── 検索インデックス・タグページの統合

Phase 3: 検索・リンク強化 — MkDocs 移行（将来）
  ├── MkDocs 導入 + テーマ設定
  ├── 既存 Markdown の互換性確保
  ├── 全文検索 + カテゴリナビ + 相互リンク
  └── GitHub Actions のビルドパイプライン統合
```

### 最小構成で何から始めるべきか

**Phase 1 の中核は以下の 4 ステップ:**

1. `claude/` ディレクトリ + カテゴリ構造の作成
2. 記事テンプレート（frontmatter 仕様）の確定
3. build_site.py への `build_claude_pages()` 追加 + ナビ統合
4. 初期コンテンツの手動作成（2-3 記事）

---

## 7. Initial File Proposal

### Phase 1 で作成するファイル

**ディレクトリ構造:**

```
claude/
├── README.md                     全体目次・カテゴリ説明
├── _template.md                  新規記事テンプレート
├── releases/
│   └── claude-code-updates.md    Claude Code のリリース情報（蓄積型）
├── guides/
│   └── setup.md                  セットアップガイド
├── tools/
│   └── comparison.md             ツール比較（Claude Code / Cursor / Cowork）
└── prompts/
    └── templates.md              プロンプトテンプレート集
```

**各ファイルの役割:**

| ファイル | 役割 |
|----------|------|
| `claude/README.md` | Claude セクションの入口。カテゴリ一覧・更新ルール・方針 |
| `claude/_template.md` | 新規記事作成時の雛形（frontmatter + セクション構成） |
| `claude/releases/claude-code-updates.md` | Claude Code の更新情報を日付付きで蓄積 |
| `claude/guides/setup.md` | Claude Code / Console のセットアップ手順 |
| `claude/tools/comparison.md` | ツール比較表（用途・コスト・得意分野） |
| `claude/prompts/templates.md` | よく使うプロンプトのテンプレート集 |

**変更する既存ファイル:**

| ファイル | 変更内容 |
|----------|----------|
| `scripts/build_site.py` | `build_claude_pages()` 追加 + `page_shell()` のナビに「Claude Info」追加 + `main()` に呼び出し追加 |
| `README.md` | 「関連ドキュメント」に Claude セクションへのリンク追加。ディレクトリ構成に `claude/` を追加 |
| `docs/HANDOFF.md` | Key Files に claude/ 関連を追記。Remaining Roadmap に Phase 2/3 を追加 |

**Frontmatter 仕様:**

```yaml
---
title: "Claude Code 2026年3月アップデート"
category: releases           # releases / guides / tools / prompts / troubleshooting / ecosystem
subcategory: claude-code     # カテゴリ内のサブ分類
tags: [claude-code, release, v2.x]
date: 2026-03-23             # 作成日
updated: 2026-03-23          # 最終更新日
sources:                     # 情報ソース（重複チェック・トレーサビリティ用）
  - url: "https://..."
    title: "ソースのタイトル"
    date: 2026-03-22
---
```

### Phase 2 で追加するファイル

| ファイル | 役割 |
|----------|------|
| `data/claude_feeds.yaml` | Claude 関連の情報ソース定義（RSS URL・スクレイピング対象） |
| `data/claude_seen_urls.json` | 重複排除用 URL 履歴 |
| `scripts/claude_main.py` | 収集パイプライン統括 |
| `scripts/claude_collect.py` | RSS/スクレイピングで情報収集 |
| `scripts/claude_summarize.py` | Claude API で日本語要約 + カテゴリ自動分類 |
| `scripts/claude_render.py` | カテゴリ別 Markdown への追記/新規生成 |
| `.github/workflows/claude-info.yml` | 日次自動実行ワークフロー |

### Phase 2 の収集ソース候補

| ソース | タイプ | URL |
|--------|--------|-----|
| Anthropic News | site | https://www.anthropic.com/news |
| Anthropic Engineering Blog | rss | https://www.anthropic.com/engineering/rss.xml（要確認） |
| Claude Code GitHub Releases | api | GitHub API で releases を取得 |
| Claude Docs Changelog | site | https://docs.anthropic.com/changelog（要確認） |
| Anthropic X (Twitter) | api/site | 要検討 |
| Reddit r/ClaudeAI | rss | https://www.reddit.com/r/ClaudeAI/.rss |
| Qiita (claude タグ) | rss | https://qiita.com/tags/claude/feed |
| Zenn (claude トピック) | rss | https://zenn.dev/topics/claude/feed |

---

## 8. Risks / Notes

### パイプラインへの影響

- **build_site.py の改修リスク**: `build_model_page()` と同じパターンで `build_claude_pages()` を追加する方式なら、既存ロジックへの影響は最小。`main()` に1行追加するだけ
- **page_shell() のナビ変更**: 全ページに影響するが、リンクを1つ追加するだけなので低リスク
- **検索インデックス**: `build_search_index()` に claude/ の記事を追加する必要があるが、既存の news/ 記事の検索に影響しない

### 重複排除の設計上の注意

- **URL ベース**: 既存の `seen_urls.py` のパターンを流用。ただし `claude_seen_urls.json` として分離（既存日報の URL 履歴と混ぜない）
- **内容ベース**: 同じトピック（例: Claude Code v2.5 リリース）が複数ソースから来る場合、最初の記事に情報を統合する方式が望ましい。これは Phase 2 で Claude API の要約時に「既存記事との重複チェック」を行うことで実現
- **蓄積型の更新**: カテゴリページは日付セクション（`## 2026-03-23`）で追記していく形式。過去の内容は消さない

### セキュリティ / 秘匿情報

- 公開サイトに含めるため、API キー・個人情報・内部メモが混入しないよう注意
- `claude/_drafts/` ディレクトリを gitignore に追加し、下書き・非公開メモの退避場所にする
- frontmatter の `sources` にはパブリック URL のみ記載

### Git 運用

- `claude/` のコンテンツは手動コミット（Phase 1）→ 自動コミット（Phase 2）
- Phase 2 の自動コミット対象: `claude/`, `data/claude_seen_urls.json`
- daily-news.yml の `git add` 対象には含めない（別ワークフロー or 統合を検討）

### README.md / HANDOFF.md 更新の必要性

**README.md:**
- 「主な機能」に Claude エコシステム情報の記述を追加
- 「ディレクトリ構成」に `claude/` を追加
- 「関連ドキュメント」に Claude セクションへのリンクを追加

**HANDOFF.md:**
- Section 1 (Overview) に Claude 情報パイプラインの概要を追加
- Section 4 (Key Files) に新規スクリプト・データファイルを追加
- Section 5 (Data Flow) に Claude 収集フローを追加
- Section 8 (Remaining Roadmap) に Phase 2/3 を planned として追加

---

## 9. 次に Claude Code に依頼すべき実装プロンプト案

### Phase 1 実装プロンプト（推奨）

```
以下の仕様で、Claude エコシステム情報セクションの Phase 1（最小構成）を実装してください。

## 概要
既存の AI News サイトに「Claude Info」セクションを追加します。
claude/ ディレクトリにカテゴリ別の Markdown を配置し、
build_site.py を拡張して _site/claude/ に HTML を生成します。

## 作成するファイル（新規）
1. claude/README.md — カテゴリ一覧・方針
2. claude/_template.md — 記事テンプレート
3. claude/releases/claude-code-updates.md — 初期コンテンツ（Claude Code の最新情報）
4. claude/guides/setup.md — セットアップガイド
5. claude/tools/comparison.md — ツール比較

## 変更するファイル（既存）
1. scripts/build_site.py:
   - build_claude_pages() 関数を追加（claude/ の Markdown → _site/claude/ の HTML）
   - page_shell() のナビに「Claude Info」リンクを追加
   - main() に build_claude_pages() 呼び出しを追加
   - 検索インデックスに claude 記事を含める
2. README.md: ディレクトリ構成と関連ドキュメントを更新
3. docs/HANDOFF.md: Key Files と Roadmap を更新

## 制約
- 既存のニュースパイプライン（scripts/main.py 等）には一切触れない
- 既存のサイト生成ロジック（日報・モデル・タグ・検索）を壊さない
- build_model_page() の実装パターンを参考にする
- CSS は既存のダークテーマに統一
- frontmatter 仕様: title / category / subcategory / tags / date / updated / sources
- カテゴリ別のサイドナビを _site/claude/index.html に配置

## 参考ファイル
- scripts/build_site.py の build_model_page()（新セクション追加の実績パターン）
- scripts/build_site.py の page_shell()（ナビゲーション構造）
- data/feeds.yaml（ソース定義のフォーマット参考）

## 回帰確認
実装後に以下を確認:
1. python -m scripts.build_site が正常に完了すること
2. _site/claude/index.html が生成されること
3. _site/index.html のナビに「Claude Info」が表示されること
4. 既存の日報・モデルページが壊れていないこと
```
