# AI News Daily

世界中の AI ニュースを毎日自動で収集・要約し、日本語の日報として静的サイトに公開するパイプラインです。

22 のソース（US / JP / CN / techblog / research）から RSS とスクレイピングで記事を収集し、Claude API で日本語要約・重要度スコア・タグを付与して Markdown 日報を生成します。GitHub Actions で毎日自動実行し、GitHub Pages にデプロイします。

---

## 主な機能

- **ニュース収集** — 22 ソース / 5 リージョンから RSS + サイトスクレイピングで自動収集
- **重複排除** — 既出 URL の自動スキップ + ソースペナルティ（同じ記事が繰り返されるソースを一時停止）
- **本文取得** — 記事 URL から本文を抽出し、キャッシュ。取得失敗時は RSS summary をフォールバック
- **AI 要約** — Claude API（claude-sonnet-4-5）で日本語要約・重要度スコア（1-10）・タグを付与
- **日報生成** — 「今日の総括」「注目3件」「リージョン別記事」を含む Markdown 日報を自動出力
- **静的サイト** — Linear.app 風ダークテーマの HTML サイトを生成（3カラムレイアウト・月別アーカイブ・タグ・検索・モデル一覧・レスポンシブ対応）
- **モデルまとめ** — 最新 AI モデルの性能ランキング・コスト比較・カテゴリ別一覧を手動生成
- **Claude エコシステム情報** — Claude / Claude Code / Console / 関連ツールの最新情報をカテゴリ別に整理・公開
- **収集メトリクス** — ソース別件数・本文取得率・要約成功率を日次蓄積。異常検知 + index.html バナー表示

---

## ディレクトリ構成

```
scripts/
  main.py              日報パイプライン統括
  collect.py           RSS/サイトスクレイピング
  seen_urls.py         既出URL管理・ペナルティ
  fetch_body.py        記事本文取得・キャッシュ
  summarize.py         Claude API 要約・スコア・タグ
  cluster_topics.py    記事クラスタリング
  render_markdown.py   Markdown 日報生成
  build_index.py       index.md 生成
  build_site.py        静的HTMLサイト生成
  model_report.py      AIモデルまとめパイプライン
  collect_models.py    モデル情報収集
  render_model_report.py モデルまとめMarkdown生成
  config.py            設定読み込み
  metrics.py           メトリクス保存・表示・健全性チェック
  test_collect.py      ソース収集テスト
  test_pipeline.py     テスト用パイプライン（モデル比較）

data/
  feeds.yaml           情報ソース定義
  config.yaml          設定値（オプション、デフォルト値あり）
  seen_urls.json       既出URL履歴・ペナルティ
  metrics.json         日次メトリクス（自動蓄積）
  cache/               本文キャッシュ（日次リセット）

news/YYYY/MM/          日報Markdown
models/                AIモデルまとめ
claude/                Claudeエコシステム情報（カテゴリ別Markdown）
  releases/            リリース情報
  guides/              セットアップ・ワークフローガイド
  tools/               ツール比較
  prompts/             プロンプトテンプレート
  troubleshooting/     トラブルシューティング
  ecosystem/           エコシステム全般
_site/                 生成された静的サイト（Linear風3カラムUI）
  month/               月別アーカイブページ
linear_ui_refs_optimized/  UIデザイン参考画像

.github/workflows/
  daily-news.yml       毎日自動実行 → Pages デプロイ
  model-report.yml     モデルまとめ手動実行
  deploy-pages.yml     Pages 再デプロイ
```

---

## セットアップ

```bash
git clone https://github.com/luster88/ai-news-system.git
cd ai-news-system

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 環境変数

`.env` ファイルをプロジェクトルートに作成してください。

```
ANTHROPIC_API_KEY=sk-ant-...
```

---

## 使い方

### 日報パイプライン（メイン）

```bash
python -m scripts.main
```

収集 → 要約 → Markdown 生成 → メトリクス保存まで一括実行します。出力は `news/YYYY/MM/YYYY-MM-DD.md` に保存されます。

### 静的サイト生成

```bash
python -m scripts.build_site
```

`_site/` に HTML サイトを生成します。日報一覧（月別アーカイブ付き）・記事詳細・タグ・検索・モデルまとめ・Claude 情報ページを含みます。

### ソース収集テスト

```bash
python -m scripts.test_collect              # 全ソース
python -m scripts.test_collect us           # リージョン指定
python -m scripts.test_collect "OpenAI"     # ソース名で検索
python -m scripts.test_collect --penalties  # ペナルティ状況付き
```

API キー不要で、各ソースの収集結果を即座に確認できます。

### メトリクス・健全性チェック

```bash
python -m scripts.metrics              # サマリ + 詳細 + 健全性チェック
python -m scripts.metrics --latest     # 最新回の詳細のみ
python -m scripts.seen_urls            # ペナルティ状況確認
```

### モデルまとめ

```bash
python -m scripts.model_report
```

AI モデルの性能ランキング・コスト比較を収集し、`models/latest.md` に出力します。

### Claude エコシステム情報

```bash
python -m scripts.claude_main
```

Claude / Claude Code / Console 関連の最新情報を自動収集し、`claude/` 配下にカテゴリ別 Markdown として書き出します。GitHub Actions (`claude-info.yml`) で毎日 JST 07:00 に自動実行されます。

### テスト用パイプライン（モデル比較）

```bash
python -m scripts.test_pipeline                          # sonnet（デフォルト）
python -m scripts.test_pipeline --model claude-opus-4-6  # opus で比較
```

ペナルティなしで全件収集し、`test-{model}-{date}-{HHMM}.md` として出力します。seen_urls は更新されません。

---

## 出力物

| パス | 内容 |
|---|---|
| `news/YYYY/MM/YYYY-MM-DD.md` | 日報 Markdown |
| `news/YYYY/MM/test-*.md` | テスト出力（モデル比較用） |
| `news/YYYY/MM/prev-*.md` | 保存記事 |
| `models/latest.md` | 最新 AI モデルまとめ |
| `models/history/` | モデルまとめの過去スナップショット |
| `_site/` | 静的 HTML サイト（Linear風UI） |
| `_site/month/YYYY-MM/` | 月別アーカイブページ |
| `data/metrics.json` | 日次メトリクス（ソース別件数・成功率等） |
| `index.md` | Markdown インデックス |

---

## 運用

- **日次自動実行**: GitHub Actions (`daily-news.yml`) が毎日 JST 01:05 に実行し、日報生成 → コミット → GitHub Pages にデプロイ
- **モデルまとめ**: GitHub Actions (`model-report.yml`) から手動実行（`workflow_dispatch`）
- **Pages 再デプロイ**: `deploy-pages.yml` から手動実行
- **メトリクス**: パイプライン実行時に `data/metrics.json` へ自動蓄積。`python -m scripts.metrics` で閲覧
- **健全性チェック**: 0件連続ソース・本文取得率低下・件数急落を自動検知し、CLI 警告 + サイトのバナーで通知

---

## 注意事項

- **Claude API キーが必要です** — `main`, `model_report`, `test_pipeline` の実行には `ANTHROPIC_API_KEY` が必要
- **一部サイトでは本文取得に制限があります** — OpenAI は 403、JS レンダリング必須のサイトは取得失敗（RSS summary でフォールバック）
- **arXiv RSS は週末に 0 件になります** — 正常動作です。月曜日にまとめて配信されます
- **設定は `data/config.yaml` で変更可能です** — ファイルがなくてもデフォルト値で動作します

---

## 関連ドキュメント

- **[docs/HANDOFF.md](docs/HANDOFF.md)** — 引き継ぎドキュメント。実装状況・データフロー・残タスク・既知の制約を詳細に記載
- **[claude/README.md](claude/README.md)** — Claude エコシステム情報セクション。カテゴリ一覧・方針・frontmatter 仕様
- **[docs/claude-code-kb-plan.md](docs/claude-code-kb-plan.md)** — Claude 情報サイトの設計・計画書
