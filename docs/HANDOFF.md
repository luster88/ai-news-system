# HANDOFF.md — AI News System 引き継ぎドキュメント

最終更新: 2026-03-24（第4版）

---

## 1. Overview

AIニュースを自動収集・要約し、静的サイトとして公開するパイプライン。

**全体フロー:**

```
feeds.yaml (22ソース, 5リージョン)
  → collect_articles()        RSS/サイトスクレイピング
  → filter_seen_articles()    既出URL除外
  → compute_source_penalties() ペナルティ計算
  → apply_source_penalties()  ペナルティ中ソース除外
  → fetch_article_bodies()    記事本文取得・キャッシュ
  → summarize_articles()      Claude API で日本語要約・スコア・タグ付与
  → cluster_articles()        Jaccard類似度でクラスタリング
  → render_daily_markdown()   news/YYYY/MM/YYYY-MM-DD.md 出力（ペナルティ状況付き）
  → build_index()             index.md 更新
  → build_site()              _site/ に静的HTML生成（健全性バナー付き）
  → save_metrics()            data/metrics.json にメトリクス蓄積
```

別パイプラインとして:
- **最新AIモデルまとめ** — 手動実行でモデル情報をまとめたレポートを生成
- **Claude エコシステム情報** — Claude/Claude Code/Console 関連の最新情報を日次自動収集・カテゴリ別整理・サイト公開
- **テスト用パイプライン** — ペナルティなし全件収集 + モデル比較用 test- ファイル出力
- **メトリクス閲覧** — `python -m scripts.metrics` で収集精度・健全性を確認

**Claude エコシステム情報パイプライン:**

```
claude_feeds.yaml (official/community/tools グループ)
  → collect_claude_articles()      RSS/サイトスクレイピング + キーワードフィルタ
  → filter_seen_articles()         claude_seen_urls.json と照合
  → apply_source_penalties()       ペナルティ中ソース除外
  → fetch_article_bodies()         記事本文取得（既存モジュール再利用）
  → summarize_claude_articles()    Claude API で要約 + カテゴリ自動分類 + タグ付与
  → render_claude_articles()       claude/{category}/{slug}.md に追記 or 新規生成
  → build_claude_pages()           _site/claude/ に HTML 生成
```

---

## 2. Current Status

**フェーズ: 安定運用（拡張可能段階）**

- **日報パイプライン**: 運用中。GitHub Actions で毎日 JST 01:05 に自動実行。
- **モデルまとめ**: 週次自動実行（毎週月曜、`daily-news.yml` に組み込み）+ 手動実行（`model-report.yml`）。
- **Claude エコシステム情報**: 運用中。GitHub Actions で毎日 JST 07:00 に自動実行（`claude-info.yml`）。
- **静的サイト**: 運用中。GitHub Pages にデプロイ済み。Linear.app 風UIに全面リデザイン完了。
- **UIリデザイン**: カード型ブログUI → Linear風3カラムダッシュボードに全面変更。月別アーカイブ・年月折りたたみサイドバー・レスポンシブ対応 完了。
- **ソース**: 22ソース / 5リージョン。実効稼働率 91%（arXiv 2本は週末 0件）。
- **安全性修正**: HIGH 5件 + MEDIUM 5件 完了。
- **中期タスク**: 5件すべて完了。
- **要約品質改善**: 4件（RSS フォールバック、スコア基準、system prompt、キーワード拡充）完了。
- **Claude エコシステム改善**: 404リンク解消・テーブルCSS共通化・カテゴリ概要表示・記事概要表示 完了。
- **本文抽出改善**: ソース別セレクタ（Qiita/Zenn/TechCrunch）追加 完了。

既知の制約:
- JS レンダリングが必要なサイト（一部 CN ソース）では本文取得に失敗する（`body=""` でフォールバック）
- OpenAI の公式サイトは 403 でスクレイピング不可（RSS summary フォールバックで軽減）
- `requirements.txt` のバージョン未固定（CI 再現性リスク）

---

## 3. Completed Work

### HIGH priority 修正 (done)

| 修正内容 | 対象ファイル |
|---|---|
| API キー早期チェック | `scripts/main.py` |
| タグ名パストラバーサル防止 | `scripts/build_site.py` (`_sanitize_dirname`) |
| Claude API タイムアウト設定 (120s/180s) | `scripts/summarize.py`, `scripts/model_report.py` |
| タイムゾーン UTC 統一 | `scripts/render_markdown.py` |
| seen_urls.json アトミック書き込み | `scripts/seen_urls.py` |

### MEDIUM priority 修正 (done)

| 修正内容 | 対象ファイル |
|---|---|
| JSON パース失敗時のフォールバック改善 (`[解析失敗]` + 200文字切り詰め) | `scripts/summarize.py` |
| `compute_source_penalties` 未使用引数 `raw_articles` 削除 | `scripts/seen_urls.py`, `scripts/main.py` |
| RSS bozo フラグチェック追加 | `scripts/collect.py` |
| fetch_body HTTP リトライ (429/503, 最大2回) | `scripts/fetch_body.py` |
| 未使用依存 `firecrawl-py` 削除 | `requirements.txt` |

### 中期タスク (done)

| # | タスク | 対象ファイル |
|---|---|---|
| 1 | `_request_html` HTTP リトライ追加 | `scripts/collect.py` |
| 2 | リンク抽出ロジック統合 (`_extract_links` 共通ヘルパー) | `scripts/collect.py` |
| 3 | config.yaml 集約 Phase A (Tier 1 定数 11項目) | `data/config.yaml`, `scripts/config.py`, 6モジュール |
| 4 | パイプライン実行ログ改善 (時刻/実行時間/API回数/キャッシュ内訳) | `scripts/main.py`, `scripts/model_report.py`, `scripts/summarize.py`, `scripts/fetch_body.py` |
| 5 | test_collect `--penalties` ドライラン | `scripts/test_collect.py` |

### 要約品質改善 (done)

| 改善内容 | 対象ファイル |
|---|---|
| 本文取得失敗時に RSS summary をフォールバック本文として全リージョンに適用 | `scripts/summarize.py` |
| importance_score の評価基準を5段階で明示 | `scripts/summarize.py` |
| system prompt で JSON 出力安定化・フォーマット遵守を指示 | `scripts/summarize.py` |
| GOOD_AI_KEYWORDS に AI 技術手法・モデル名・日本語 10語追加（計42語） | `scripts/collect.py` |
| 今日の総括の max_tokens 300→500（途切れ修正） | `scripts/summarize.py` |

### 機能追加 (done)

| 機能 | 対象ファイル |
|---|---|
| techblog リージョン追加 (Qiita, Zenn, nyosegawa) | `data/feeds.yaml`, `scripts/collect.py`, `scripts/summarize.py`, `scripts/render_markdown.py` |
| prev- ファイルの別カテゴリ表示 | `scripts/build_site.py`, `scripts/build_index.py` |
| 最新AIモデルまとめ機能 | `scripts/model_report.py`, `scripts/collect_models.py`, `scripts/render_model_report.py` |
| モデルまとめのサイト統合 (ナビリンク, テーブルスタイル, 過去レポート) | `scripts/build_site.py`, `scripts/build_index.py` |
| 手動実行ワークフロー | `.github/workflows/model-report.yml` |
| テスト用パイプライン (`--model` 比較, test- ファイル出力, index 連携) | `scripts/test_pipeline.py`, `scripts/render_markdown.py`, `scripts/summarize.py`, `scripts/build_site.py`, `scripts/build_index.py` |
| ペナルティ状況の可視化 (専用コマンド・test_collect 強化・日報セクション) | `scripts/seen_urls.py`, `scripts/test_collect.py`, `scripts/render_markdown.py`, `scripts/main.py` |
| 情報ソース整理 (壊れた5ソース削除・3ソース新規追加・Verge URL修正) | `data/feeds.yaml`, `scripts/collect.py` |
| `requirements.txt` バージョン範囲固定（直接依存9パッケージ） | `requirements.txt` |
| Claude エコシステム情報セクション Phase 1（カテゴリ別ページ・サイト統合・ナビ・検索） | `scripts/build_site.py`, `claude/` ディレクトリ, `README.md` |
| Claude 記事内リンク404解消（`.md` 相対リンクの HTML パス変換） | `scripts/build_site.py`（`_rewrite_claude_md_links` 追加） |
| テーブル CSS 共通化（`.model-report` スコープ → `.article-body` 共通） | `scripts/build_site.py` |
| 未作成カテゴリディレクトリ追加（prompts / troubleshooting / ecosystem） | `claude/` 配下に `.gitkeep` |
| Claude インデックスにカテゴリ概要セクション追加（6カテゴリの説明・件数表示） | `scripts/build_site.py`（`_CLAUDE_CATEGORIES` 3要素化） |
| Claude 記事一覧に概要テキスト表示（`_claude_summary_from_body` 追加） | `scripts/build_site.py` |
| Claude カテゴリ概要を折りたたみ式に変更（`<details>/<summary>`、デフォルト閉じ） | `scripts/build_site.py` |
| Claude 記事一覧を日付ごとにグループ化表示（日付見出し + 件数、降順ソート） | `scripts/build_site.py` |

### 静的サイト UI 全面リデザイン (done)

| 改善内容 | 対象ファイル |
|---|---|
| カード型ブログUI → Linear.app 風3カラムリスト型UIに全面変更 | `scripts/build_site.py` (CSS + HTML テンプレート) |
| 左サイドバー: 年/月折りたたみツリーナビ (`<details>/<summary>`) | `scripts/build_site.py` (`_build_date_tree`) |
| 月別アーカイブページ生成 (`_site/month/YYYY-MM/index.html`) | `scripts/build_site.py` (`_build_month_tabs`, `_collect_months`) |
| content-header に月タブUI (All / 2026-03 / ...) | `scripts/build_site.py` |
| 記事詳細ページの本文中央寄せ (max-width:800px, margin:0 auto) | `scripts/build_site.py` (CSS `.article-detail`) |
| 1行リスト型アイテム (タイトル→要約→メタ+タグ の縦配置) | `scripts/build_site.py` (`_item_html`) |
| タグを控えめ表示 (背景なし, 低コントラスト, `·` 区切り) | `scripts/build_site.py` (CSS `.tag`) |
| ダークテーマ統一 (#0f0f12 背景, shadow/gradient 禁止) | `scripts/build_site.py` (CSS 全体) |
| レスポンシブ対応: モバイル1カラム + ハンバーガーメニュー | `scripts/build_site.py` (CSS `@media`, JS `#menu-toggle`) |
| 命名統一: Issues → AI News / All Issues → All AI News | `scripts/build_site.py` (page_shell, build_index_pages) |
| 0件カテゴリのリンク無効化 (ERR_FILE_NOT_FOUND 修正) | `scripts/build_site.py` (build_claude_pages) |
| メインカラム max-width:860px + margin:auto で重心調整 | `scripts/build_site.py` (CSS `.content-area > *`) |
| topbar ナビ (AI News / Claude / Models / Tags / Search) | `scripts/build_site.py` (page_shell) |
| 最新記事の視覚強調 (accent ドット + 白文字) | `scripts/build_site.py` (CSS `.list-row:first-child`) |

### 収集精度メトリクス (done)

| Phase | 内容 | 対象ファイル |
|---|---|---|
| Phase 1 | メトリクス蓄積基盤（`data/metrics.json` に日次保存、アトミック書き込み） | `scripts/metrics.py`（新規）, `scripts/main.py` |
| Phase 2 | ソース別収集件数の記録（`collect_articles()` の戻り値を `(articles, source_stats)` に拡張） | `scripts/collect.py`, `scripts/main.py`, `scripts/test_pipeline.py` |
| Phase 3 | メトリクス表示コマンドの拡充（日次サマリ + 最新詳細 + ソース別件数 + CLI オプション） | `scripts/metrics.py` |
| Phase 4 | ソース健全性の異常検知（0件連続・本文取得率低下・件数急落を検知、CLI 警告 + index.html バナー） | `scripts/metrics.py`, `scripts/build_site.py` |

**記録項目**: 総収集数 / 新規・既出・ペナルティ除外数 / ソース別件数 / 0件ソース / 本文取得成功率 / [暫定]・[解析失敗]件数 / importance分布 / 実行時間

**異常検知ルール**:

| ルール | 閾値 | タイプ |
|---|---|---|
| 0件連続ソース | 3日連続 | `zero_streak` |
| 本文取得率低下 | 50% 未満 | `body_rate_low` |
| 収集件数急落 | 直近3日平均の30%以下 | `count_drop` |

---

## 4. Key Files

### エントリポイント

| ファイル | 実行コマンド | 用途 |
|---|---|---|
| `scripts/main.py` | `python -m scripts.main` | 日報パイプライン全体 |
| `scripts/model_report.py` | `python -m scripts.model_report` | モデルまとめ生成 |
| `scripts/test_pipeline.py` | `python -m scripts.test_pipeline [--model ...]` | テスト用パイプライン（ペナルティなし・モデル比較） |
| `scripts/build_site.py` | `python -m scripts.build_site` | 静的サイト再ビルド（Linear風UI・月別ページ・レスポンシブ） |
| `scripts/build_index.py` | `python -m scripts.build_index` | index.md のみ再生成 |
| `scripts/test_collect.py` | `python -m scripts.test_collect [args]` | ソース収集テスト |
| `scripts/seen_urls.py` | `python -m scripts.seen_urls` | ペナルティ状況確認 |
| `scripts/metrics.py` | `python -m scripts.metrics [--latest] [--days N]` | メトリクス閲覧・健全性チェック |

### パイプラインモジュール

| ファイル | 役割 |
|---|---|
| `scripts/collect.py` | RSS/サイトスクレイピング (22ソース, 5リージョン) |
| `scripts/seen_urls.py` | 既出URL管理・ソースペナルティ・状況表示 |
| `scripts/fetch_body.py` | 記事本文取得・キャッシュ |
| `scripts/summarize.py` | Claude API 要約・スコア・タグ付与（system prompt + 5段階基準） |
| `scripts/cluster_topics.py` | Jaccard 類似度クラスタリング |
| `scripts/render_markdown.py` | 日報 Markdown 生成（ペナルティ状況セクション付き） |
| `scripts/collect_models.py` | モデル情報収集 (日報解析 + スクレイピング) |
| `scripts/render_model_report.py` | モデルまとめ Markdown 生成 |
| `scripts/config.py` | 設定ファイル読み込み（デフォルトフォールバック付き） |
| `scripts/metrics.py` | メトリクス保存・表示・健全性チェック |

### Claude エコシステム情報

| ファイル | 内容 |
|---|---|
| `scripts/claude_main.py` | Claude 情報パイプライン統括（`python -m scripts.claude_main`） |
| `scripts/claude_collect.py` | Claude 関連ソースからの記事収集（RSS/サイトスクレイピング + キーワードフィルタ） |
| `scripts/claude_summarize.py` | Claude API で要約 + カテゴリ自動分類 + タグ付与 |
| `scripts/claude_render.py` | カテゴリ別 Markdown への追記 / 新規生成 |
| `data/claude_feeds.yaml` | Claude 関連の情報ソース定義（official / community / tools グループ） |
| `data/claude_seen_urls.json` | Claude パイプライン専用の既出URL履歴（日報とは分離） |
| `claude/README.md` | セクション全体の目次・方針・frontmatter 仕様 |
| `claude/{category}/*.md` | カテゴリ別の Markdown 記事（releases / guides / tools / prompts / troubleshooting / ecosystem） |
| `claude/_template.md` | 新規記事作成テンプレート |
| `.github/workflows/claude-info.yml` | 毎日 JST 07:00 自動実行 + 手動実行 |

### 設定・データ

| ファイル | 内容 |
|---|---|
| `data/config.yaml` | Tier 1 設定値 11項目 (なくてもデフォルト値で動作) |
| `data/feeds.yaml` | 情報ソース定義 (5リージョン, 22ソース) |
| `data/seen_urls.json` | 既出URL履歴 + ソースペナルティ (git管理) |
| `data/metrics.json` | 日次実行メトリクス（パイプライン実行時に自動蓄積、daily-news.yml でコミット） |
| `data/cache/` | 記事本文キャッシュ (gitignore済み, 日次リセット) |
| `.env` | `ANTHROPIC_API_KEY` (gitignore済み) |

### GitHub Actions

| ファイル | トリガー | 内容 |
|---|---|---|
| `.github/workflows/daily-news.yml` | 毎日 JST 01:05 + 手動 | 日報生成 → コミット（news/, index.md, seen_urls.json, metrics.json）→ Pages デプロイ |
| `.github/workflows/model-report.yml` | 手動のみ | モデルまとめ生成 → コミット → Pages デプロイ |
| `.github/workflows/deploy-pages.yml` | 手動のみ | Pages 再デプロイのみ |

---

## 5. Data Flow

### 日報パイプライン

```
[feeds.yaml]
    │
    ▼
collect_articles()  ── 22ソースから記事収集
    │                  region/source/title/link/published/summary
    ▼
filter_seen_articles()  ── seen_urls.json と照合
    │                      → (new_articles, seen_articles)
    ▼
compute_source_penalties()  ── seen件数 ≥ 2 → 3日間ペナルティ
    │
    ▼
apply_source_penalties()  ── ペナルティ中ソースの記事を除外
    │
    ▼
fetch_article_bodies()  ── HTTP GET + BeautifulSoup 本文抽出
    │                      research リージョンはスキップ
    │                      本文なし時は RSS summary をフォールバック（要約時）
    │                      キャッシュ: data/cache/{date}_{hash}.txt
    │                      → article["body"] を付与
    ▼
summarize_articles()  ── Claude API (claude-sonnet-4-5)
    │                    system prompt + 5段階 importance 基準
    │                    最大25記事 × 1 API call + 1 overall
    │                    → summary_ja / importance_score / tags / why_it_matters
    ▼
cluster_articles()  ── Jaccard 類似度 ≥ 0.45 でグルーピング
    │                  → related_articles を付与
    ▼
render_daily_markdown()  ── news/YYYY/MM/YYYY-MM-DD.md 出力
    │                       末尾にペナルティ状況テーブル
    ▼
build_index()  ── index.md 更新
    │
    ▼
update_seen_urls()  ── 新規URLを seen_urls.json に記録 (アトミック書き込み)
    │
    ▼
save_metrics()  ── data/metrics.json にソース別件数・本文成功率・要約統計を蓄積
                   build_site() で健全性バナーに反映
```

### モデルまとめパイプライン

```
[news/*.md 直近14日分]  ── モデル関連記事を抽出 (MODEL_KEYWORDS でフィルタ)
[Anthropic/Google/Artificial Analysis]  ── 料金・ベンチマーク情報スクレイピング
    │
    ▼
structure_model_info()  ── Claude API (max_tokens=8000)
    │                      → ranking / pricing / categories / new_updates
    ▼
render_model_report()  ── models/latest.md + models/history/YYYY-MM-DD.md
```

### テスト用パイプライン

```
python -m scripts.test_pipeline [--model claude-opus-4-6]
    │
    ▼
collect_articles()  ── ペナルティなし全件収集
    ▼
fetch_article_bodies()
    ▼
summarize_articles(model_override=...)  ── 任意モデルで要約
    ▼
render_daily_markdown(filename_override="test-{model}-{date}-{HHMM}")
    ── seen_urls 更新なし、index 更新なし
```

---

## 6. Runbook

### セットアップ

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows

pip install -r requirements.txt

# .env ファイルを作成
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
```

### 実行コマンド

```bash
# 日報パイプライン全体 (API キー必要)
python -m scripts.main

# モデルまとめ生成 (API キー必要)
python -m scripts.model_report

# テスト用パイプライン (API キー必要)
python -m scripts.test_pipeline                        # sonnet (デフォルト)
python -m scripts.test_pipeline --model claude-opus-4-6  # opus 比較

# 静的サイトのみ再ビルド (API キー不要)
python -m scripts.build_site

# index.md のみ再生成 (API キー不要)
python -m scripts.build_index

# ソース収集テスト (API キー不要)
python -m scripts.test_collect              # 全ソース
python -m scripts.test_collect us           # リージョン指定
python -m scripts.test_collect "OpenAI"     # ソース名部分一致
python -m scripts.test_collect --penalties  # seen_urls フィルタ結果表示

# ペナルティ状況確認 (API キー不要)
python -m scripts.seen_urls

# メトリクス閲覧・健全性チェック (API キー不要)
python -m scripts.metrics              # サマリ + 最新詳細 + 健全性チェック
python -m scripts.metrics --latest     # 最新回の詳細のみ
python -m scripts.metrics --days 7     # 直近7件のサマリ
```

### Claude エコシステム情報パイプライン

```bash
# Claude 情報の収集・要約・Markdown 書き出し (API キー必要)
python -m scripts.claude_main
```

### 回帰確認の最低限コマンド

```bash
# 1. 収集が動くか（新規ソース含む）
python -m scripts.test_collect "TechCrunch"
python -m scripts.test_collect "Decoder"

# 2. サイトビルドが通るか
python -m scripts.build_site

# 3. config 読み込みが動くか
python -c "from scripts.config import get as cfg; print(cfg('model', 'OK'))"

# 4. ペナルティ表示が動くか
python -m scripts.seen_urls

# 5. メトリクス表示が動くか
python -m scripts.metrics
```

---

## 7. Known Caveats / Risks

### Claude パイプライン固有のリスク

| 箇所 | リスク | 対処 |
|---|---|---|
| `claude_collect.py` の `CLAUDE_SOURCE_SELECTORS` | Anthropic サイトの HTML 構造変更で収集 0件 | `filter_keywords` で RSS ソースを優先 |
| `claude_summarize.py` のカテゴリ分類 | 不適切なカテゴリに分類される可能性 | 手動で Markdown ファイルを移動・修正 |
| `claude_render.py` の追記ロジック | frontmatter パースの崩れ | `_parse_frontmatter()` で YAML safe_load を使用 |
| `claude_seen_urls.json` の分離 | 日報と Claude で同じ記事が重複する可能性 | 設計上許容（異なるパイプラインの独立性を優先） |
| Reddit RSS の品質 | スパムや無関係記事が混入 | `filter_keywords` + `importance_score` フィルタで対処 |

### 壊れやすい箇所

| 箇所 | リスク | 対処 |
|---|---|---|
| `collect.py` の `SOURCE_SELECTORS` / 固有パーサー | サイト側の HTML 構造変更で収集 0件になる | `test_collect` で定期確認 |
| `summarize.py` の JSON パース | Claude の応答フォーマットが変わると `[解析失敗]` になる | system prompt + `_safe_parse_summary_json` のフォールバックで継続 |
| `collect_models.py` の日報パース | 日報の Markdown フォーマットが変わると抽出失敗 | `### N.` + `- Source:` / `- Link:` の形式に依存 |
| `model_report.py` の Claude 応答 | max_tokens=8000 でも足りない場合 JSON が途切れる | `_safe_parse_json` で空 dict フォールバック |
| `seen_urls.json` の肥大化 | 90日分のURLが蓄積 (現在 212件) | `URL_EXPIRY_DAYS` で自動クリーンアップ |
| OpenAI 公式サイト 403 | 本文取得不可（8記事全て） | RSS summary フォールバックで軽減。根本解決にはヘッドレスブラウザが必要 |
| arXiv RSS 週末 0件 | 正常動作だが月曜に集中 | 運用上の問題なし |
| `data/metrics.json` 未蓄積時 | 初回実行前はメトリクスが空。健全性チェックは3日分以上のデータが必要 | `python -m scripts.main` を実行してデータ蓄積 |

### 変更時に注意すべきポイント

- **`render_markdown.py` のセクション順序**: `build_site.py` の `_classify_model_tables` がヘッダーテキストでテーブルを分類するため、ヘッダー文言を変えるとスタイルが外れる
- **`TAG_CANDIDATES` の変更**: `summarize.py` のホワイトリスト + `build_site.py` のタグページ生成に影響
- **リージョン追加**: `feeds.yaml` + `summarize.py` の `region_order` + `render_markdown.py` のループ順序 の3箇所を同時に変更する必要がある
- **`config.yaml` のキー名**: 各モジュールの `cfg("key", default)` 呼び出しとキー名を一致させる必要がある
- **ソース削除/追加**: `feeds.yaml` のみでOK。`collect.py` の `SOURCE_SELECTORS` に固有パーサーがある場合はそちらも確認
- **`build_site.py` の CSS 変更**: CSS は `build_site.py` の `CSS` 定数に埋め込み。変更時は `python -m scripts.build_site` で `_site/style.css` を再生成する必要がある
- **月別ページの URL 構造**: `_site/month/YYYY-MM/index.html` 形式。`root_rel` は `../..` で相対パス参照
- **サイドバーツリーの `<details>` 開閉状態**: `_build_date_tree()` が現在年・現在月をデフォルト `open` に設定。月が増えても自動で正しく動作する
- **レスポンシブ CSS**: `@media(max-width:800px)` でモバイル対応。`!important` を使用している箇所があるため、スタイル上書き時は注意

### 変更時に最初に確認すべきファイル

1. `data/config.yaml` — 設定値が意図通りか
2. `data/feeds.yaml` — ソース定義が正しいか
3. `scripts/main.py` — パイプラインの流れ
4. `scripts/build_site.py` — サイト生成の全体像

---

## 8. Remaining Roadmap

### done

| タスク | 対象ファイル |
|---|---|
| collect.py _request_html リトライ | `scripts/collect.py` |
| リンク抽出ロジック統合 (_extract_links) | `scripts/collect.py` |
| config.yaml 集約 Phase A | `data/config.yaml`, `scripts/config.py`, 6モジュール |
| パイプライン実行ログ改善 | `scripts/main.py`, `scripts/model_report.py`, `scripts/summarize.py`, `scripts/fetch_body.py` |
| test_collect --penalties ドライラン | `scripts/test_collect.py` |
| HIGH priority 5件修正 | 6ファイル |
| MEDIUM priority 5件修正 | 6ファイル |
| techblog リージョン追加 | 4ファイル |
| prev- ファイル別カテゴリ表示 | 2ファイル |
| AIモデルまとめ機能 | 3ファイル新規 |
| モデルまとめサイト統合 + テーブルスタイル | `scripts/build_site.py` |
| モデルまとめ過去レポート閲覧 | `scripts/build_site.py` |
| モデルまとめ手動実行ワークフロー | `.github/workflows/model-report.yml` |
| RSS summary フォールバック（[暫定] 削減） | `scripts/summarize.py` |
| importance_score 5段階基準明示 | `scripts/summarize.py` |
| system prompt でJSON出力安定化 | `scripts/summarize.py` |
| GOOD_AI_KEYWORDS 10語追加（計42語） | `scripts/collect.py` |
| 今日の総括 max_tokens 300→500 | `scripts/summarize.py` |
| テスト用パイプライン（モデル比較・test-ファイル出力） | `scripts/test_pipeline.py` 他5ファイル |
| ペナルティ状況の可視化 | `scripts/seen_urls.py`, `scripts/test_collect.py`, `scripts/render_markdown.py`, `scripts/main.py` |
| 情報ソース整理（5削除・3追加・1修正） | `data/feeds.yaml`, `scripts/collect.py` |
| `requirements.txt` バージョン範囲固定（直接依存9パッケージ） | `requirements.txt` |
| メトリクス蓄積基盤 (Phase 1) | `scripts/metrics.py`, `scripts/main.py` |
| ソース別収集件数の記録 (Phase 2) | `scripts/collect.py`, `scripts/main.py`, `scripts/test_pipeline.py` |
| メトリクス表示コマンド拡充 (Phase 3) | `scripts/metrics.py` |
| ソース健全性の異常検知 + index.html バナー (Phase 4) | `scripts/metrics.py`, `scripts/build_site.py` |
| Claude 記事内リンク404解消（`_rewrite_claude_md_links`） | `scripts/build_site.py` |
| テーブル CSS 共通化（`.article-body table` に基本スタイル適用） | `scripts/build_site.py` |
| 未作成カテゴリディレクトリ追加（prompts / troubleshooting / ecosystem） | `claude/` 配下 |
| ソース別の本文抽出セレクタ（Qiita/Zenn/TechCrunch） | `scripts/fetch_body.py`（`SOURCE_SELECTORS` 追加） |
| model_report 週次自動実行（毎週月曜、JST曜日判定） | `.github/workflows/daily-news.yml` |
| `claude_seen_urls.json` 有効期限管理の確認 | 確認のみ: `update_seen_urls()` の `URL_EXPIRY_DAYS` が正しく適用されている |
| Claude インデックスにカテゴリ概要セクション追加 | `scripts/build_site.py` |
| Claude 記事一覧に概要テキスト表示 | `scripts/build_site.py` |
| Claude カテゴリ概要を折りたたみ式に変更 | `scripts/build_site.py` |
| Claude 記事一覧を日付グループ化表示 | `scripts/build_site.py` |
| 静的サイト UI 全面リデザイン（Linear.app 風3カラム） | `scripts/build_site.py` |
| 月別アーカイブページ生成 | `scripts/build_site.py` |
| 左サイドバー年/月折りたたみツリー | `scripts/build_site.py` |
| 記事詳細ページ本文中央寄せ | `scripts/build_site.py` |
| レスポンシブ対応（モバイル1カラム + ハンバーガーメニュー） | `scripts/build_site.py` |
| 命名統一 (Issues → AI News) | `scripts/build_site.py` |
| 0件カテゴリのリンク無効化 | `scripts/build_site.py` |
| メインカラム重心の中央寄せ調整 | `scripts/build_site.py` |

### planned

| タスク | 優先度 | 理由 |
|---|---|---|
| クラスタリング判定に summary_ja を追加 | **中** | 重複記事の検知精度向上。閾値調整が必要 |
| Claude パイプラインのメトリクス蓄積 | **中** | 日報側には `metrics.py` があるが Claude 側にはない |
| Claude パイプラインの健全性チェック | **中** | `claude_feeds.yaml` のソースが壊れても検知できない |
| モバイル検索UIの改善 | **低** | 現在モバイルではtopbar検索を非表示。Search ページリンクで代替中 |
| サイドバーのスライドインアニメーション | **低** | 現在は即時表示/非表示。`transform: translateX` でスムーズ化可能 |
| 月別ページのページネーション対応 | **低** | 月あたり30件超の場合に必要。現時点では不要 |
| config.yaml Phase B (Tier 2/3 定数移行) | **低** | Phase A で基盤完成。キーワードリスト等は変更頻度低い |
| `collect.py` の LSP 型エラー修正 | **低** | ランタイムでは問題なし |
| `source_penalties` の古いエントリ自動削除 | **低** | URLは `URL_EXPIRY_DAYS` で自動削除されるが penalties は蓄積され続ける。現時点では肥大化リスクは低い |

### planned (Claude エコシステム情報)

| タスク | 優先度 | 理由 |
|---|---|---|
| MkDocs 移行（検索・リンク強化） | **低** | Phase 3: 全文検索・カテゴリナビ・相互リンク。記事数が増えてから検討 |

### done (Claude エコシステム情報 Phase 2)

| タスク | 対象ファイル |
|---|---|
| Claude 情報の自動収集パイプライン | `scripts/claude_main.py`, `scripts/claude_collect.py`, `scripts/claude_summarize.py`, `scripts/claude_render.py` |
| `data/claude_feeds.yaml` ソース定義 | `data/claude_feeds.yaml` |
| `data/claude_seen_urls.json` 重複排除 | `data/claude_seen_urls.json`, `scripts/seen_urls.py`（file_path 引数追加） |
| `.github/workflows/claude-info.yml` 自動実行 | `.github/workflows/claude-info.yml` |

### deferred

| タスク | 理由 |
|---|---|
| `fetch_body.py` の JS レンダリングサイト対応 | Playwright 等の導入が必要。依存が大きい |
| pytest 導入 | ライブ診断 + test_pipeline で十分な段階 |
| ログを logging モジュールに移行 | print ベースで統一されており動作に問題なし |
| CSS の外部ファイル化 | `build_site.py` に埋め込み（CSS定数 約350行）。ビルド時に `_site/style.css` として出力。規模が大きくなれば分離を検討 |
| 日報の RSS フィード生成 | 需要が発生してから実装 |

---

## 9. Next Recommended Tasks

次のエージェントが最初にやるべき作業（優先順）:

1. **クラスタリング判定に summary_ja を追加** — `cluster_topics.py` の `tokenize_title` の入力を拡張し、重複記事の検知精度を向上。閾値の調整が必要。

2. **Claude パイプラインのメトリクス蓄積** — `claude_main.py` に `save_metrics()` 相当の仕組みを追加。ソース別件数・要約成功率・カテゴリ分布を記録。

3. **Claude パイプラインの健全性チェック** — `claude_feeds.yaml` のソースが0件連続した場合の警告ログ。

### UI リデザインに関する補足

`build_site.py` は CSS・HTML テンプレート・ページ生成ロジックを一体で管理している。UI を変更する場合の主要な関数:

| 関数 | 役割 |
|---|---|
| `CSS` 定数 | サイト全体のスタイル（約350行、Linear風デザインシステム） |
| `page_shell()` | 全ページ共通のHTML外枠（topbar・ナビ・モバイルメニューJS） |
| `_build_date_tree()` | 左サイドバーの年/月/日折りたたみツリー生成 |
| `_build_month_tabs()` | 月タブUI生成（All / YYYY-MM / ...） |
| `_item_html()` | 日報リスト行の HTML（タイトル→要約→メタ+タグ） |
| `_claude_article_item()` | Claude 記事リスト行の HTML |
| `build_index_pages()` | トップページ + 月別ページの生成 |
| `build_article_pages()` | 記事詳細ページの生成（本文中央寄せ） |

---

## 10. Update Rules

このドキュメントを更新すべきタイミング:

- 新しいリージョンやソースを追加したとき
- パイプラインの処理順序を変更したとき
- config.yaml にキーを追加/削除したとき
- GitHub Actions ワークフローを変更したとき
- 新しいモジュールを追加したとき
- planned / deferred タスクの状態が変わったとき
- 既知の制約や壊れやすい箇所が変わったとき
- 要約品質に影響する変更（プロンプト、max_tokens、モデル等）を行ったとき
- `claude/` のカテゴリ構造やビルド方式を変更したとき
- Claude 情報の自動収集パイプラインを追加・変更したとき
- 静的サイトの UI・レイアウト・ページ構成を変更したとき
- 月別ページやサイドバーの構造を変更したとき
