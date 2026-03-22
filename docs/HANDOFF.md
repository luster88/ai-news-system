# HANDOFF.md — AI News System 引き継ぎドキュメント

最終更新: 2026-03-22

---

## 1. Overview

AIニュースを自動収集・要約し、静的サイトとして公開するパイプライン。

**全体フロー:**

```
feeds.yaml (24ソース, 5リージョン)
  → collect_articles()        RSS/サイトスクレイピング
  → filter_seen_articles()    既出URL除外
  → compute_source_penalties() ペナルティ計算
  → apply_source_penalties()  ペナルティ中ソース除外
  → fetch_article_bodies()    記事本文取得・キャッシュ
  → summarize_articles()      Claude API で日本語要約・スコア・タグ付与
  → cluster_articles()        Jaccard類似度でクラスタリング
  → render_daily_markdown()   news/YYYY/MM/YYYY-MM-DD.md 出力
  → build_index()             index.md 更新
  → build_site()              _site/ に静的HTML生成
```

別パイプラインとして「最新AIモデルまとめ」機能があり、手動実行でモデル情報をまとめたレポートを生成する。

---

## 2. Current Status

- **日報パイプライン**: 運用可能。GitHub Actions で毎日 JST 01:05 に自動実行。
- **モデルまとめ**: 運用可能。GitHub Actions から手動実行（`workflow_dispatch`）。
- **静的サイト**: 運用可能。GitHub Pages にデプロイ済み。
- **中期タスク**: 5件すべて完了。
- **HIGH/MEDIUM priority の安全性修正**: 完了済み。

既知の制約:
- JS レンダリングが必要なサイト（一部 CN ソース）では本文取得に失敗する（`body=""` でフォールバック）
- OpenAI の公式サイトは 403 でスクレイピング不可（モデルまとめの料金情報はAnthropic/Google/Artificial Analysisから取得）

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

### 機能追加 (done)

| 機能 | 対象ファイル |
|---|---|
| techblog リージョン追加 (Qiita, Zenn, nyosegawa) | `data/feeds.yaml`, `scripts/collect.py`, `scripts/summarize.py`, `scripts/render_markdown.py` |
| prev- ファイルの別カテゴリ表示 | `scripts/build_site.py`, `scripts/build_index.py` |
| 最新AIモデルまとめ機能 | `scripts/model_report.py`, `scripts/collect_models.py`, `scripts/render_model_report.py` |
| モデルまとめのサイト統合 (ナビリンク, テーブルスタイル, 過去レポート) | `scripts/build_site.py`, `scripts/build_index.py` |
| 手動実行ワークフロー | `.github/workflows/model-report.yml` |

---

## 4. Key Files

### エントリポイント

| ファイル | 実行コマンド | 用途 |
|---|---|---|
| `scripts/main.py` | `python -m scripts.main` | 日報パイプライン全体 |
| `scripts/model_report.py` | `python -m scripts.model_report` | モデルまとめ生成 |
| `scripts/build_site.py` | `python -m scripts.build_site` | 静的サイトのみ再ビルド |
| `scripts/build_index.py` | `python -m scripts.build_index` | index.md のみ再生成 |
| `scripts/test_collect.py` | `python -m scripts.test_collect [args]` | ソース収集テスト |

### パイプラインモジュール

| ファイル | 役割 |
|---|---|
| `scripts/collect.py` | RSS/サイトスクレイピング (24ソース, 5リージョン) |
| `scripts/seen_urls.py` | 既出URL管理・ソースペナルティ |
| `scripts/fetch_body.py` | 記事本文取得・キャッシュ |
| `scripts/summarize.py` | Claude API 要約・スコア・タグ付与 |
| `scripts/cluster_topics.py` | Jaccard 類似度クラスタリング |
| `scripts/render_markdown.py` | 日報 Markdown 生成 |
| `scripts/collect_models.py` | モデル情報収集 (日報解析 + スクレイピング) |
| `scripts/render_model_report.py` | モデルまとめ Markdown 生成 |
| `scripts/config.py` | 設定ファイル読み込み |

### 設定・データ

| ファイル | 内容 |
|---|---|
| `data/config.yaml` | Tier 1 設定値 11項目 (なくてもデフォルト値で動作) |
| `data/feeds.yaml` | 情報ソース定義 (5リージョン, 24ソース) |
| `data/seen_urls.json` | 既出URL履歴 + ソースペナルティ (git管理) |
| `data/cache/` | 記事本文キャッシュ (gitignore済み, 日次リセット) |
| `.env` | `ANTHROPIC_API_KEY` (gitignore済み) |

### GitHub Actions

| ファイル | トリガー | 内容 |
|---|---|---|
| `.github/workflows/daily-news.yml` | 毎日 JST 01:05 + 手動 | 日報生成 → コミット → Pages デプロイ |
| `.github/workflows/model-report.yml` | 手動のみ | モデルまとめ生成 → コミット → Pages デプロイ |
| `.github/workflows/deploy-pages.yml` | 手動のみ | Pages 再デプロイのみ |

---

## 5. Data Flow

### 日報パイプライン

```
[feeds.yaml]
    │
    ▼
collect_articles()  ── 24ソースから記事収集
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
    │                      キャッシュ: data/cache/{date}_{hash}.txt
    │                      → article["body"] を付与
    ▼
summarize_articles()  ── Claude API (claude-sonnet-4-5)
    │                    最大25記事 × 1 API call + 1 overall
    │                    → summary_ja / importance_score / tags / why_it_matters
    ▼
cluster_articles()  ── Jaccard 類似度 ≥ 0.45 でグルーピング
    │                  → related_articles を付与
    ▼
render_daily_markdown()  ── news/YYYY/MM/YYYY-MM-DD.md 出力
    │
    ▼
build_index()  ── index.md 更新
    │
    ▼
update_seen_urls()  ── 新規URLを seen_urls.json に記録 (アトミック書き込み)
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

# 静的サイトのみ再ビルド (API キー不要)
python -m scripts.build_site

# index.md のみ再生成 (API キー不要)
python -m scripts.build_index

# ソース収集テスト (API キー不要)
python -m scripts.test_collect              # 全ソース
python -m scripts.test_collect us           # リージョン指定
python -m scripts.test_collect "OpenAI"     # ソース名部分一致
python -m scripts.test_collect --penalties  # seen_urls フィルタ結果表示
python -m scripts.test_collect --penalties "OpenAI"  # 組み合わせ可
```

### 回帰確認の最低限コマンド

```bash
# 1. 収集が動くか
python -m scripts.test_collect "Qiita"

# 2. サイトビルドが通るか
python -m scripts.build_site

# 3. config 読み込みが動くか
python -c "from scripts.config import get as cfg; print(cfg('model', 'OK'))"
```

---

## 7. Known Caveats / Risks

### 壊れやすい箇所

| 箇所 | リスク | 対処 |
|---|---|---|
| `collect.py` の `SOURCE_SELECTORS` / 固有パーサー | サイト側の HTML 構造変更で収集 0件になる | `test_collect` で定期確認 |
| `summarize.py` の JSON パース | Claude の応答フォーマットが変わると `[解析失敗]` になる | `_safe_parse_summary_json` のフォールバックで継続 |
| `collect_models.py` の日報パース | 日報の Markdown フォーマットが変わると抽出失敗 | `### N.` + `- Source:` / `- Link:` の形式に依存 |
| `model_report.py` の Claude 応答 | max_tokens=8000 でも足りない場合 JSON が途切れる | `_safe_parse_json` で空 dict フォールバック |
| `seen_urls.json` の肥大化 | 90日分のURLが蓄積 (現在 212件) | `URL_EXPIRY_DAYS` で自動クリーンアップ |

### 変更時に注意すべきポイント

- **`render_markdown.py` のセクション順序**: `build_site.py` の `_classify_model_tables` がヘッダーテキストでテーブルを分類するため、ヘッダー文言を変えるとスタイルが外れる
- **`TAG_CANDIDATES` の変更**: `summarize.py` のホワイトリスト + `build_site.py` のタグページ生成に影響
- **リージョン追加**: `feeds.yaml` + `summarize.py` の `region_order` + `render_markdown.py` のループ順序 の3箇所を同時に変更する必要がある
- **`config.yaml` のキー名**: 各モジュールの `cfg("key", default)` 呼び出しとキー名を一致させる必要がある

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

### planned

| タスク | 理由 |
|---|---|
| config.yaml Phase B (Tier 2/3 定数移行) | Phase A で基盤完成。キーワードリスト等は変更頻度が低いため優先度低 |
| `requirements.txt` のバージョン固定 | 現在ピン留めなし。再現性向上のため `pip freeze` で固定すべき |
| `collect.py` の LSP 型エラー修正 | `feedparser` / `BeautifulSoup` の戻り値型。ランタイムでは問題なし |
| `fetch_body.py` の JS レンダリングサイト対応 | Playwright 等の導入が必要。一部 CN ソースで本文取得失敗 |
| daily-news.yml への model_report 組み込み | 現在は手動実行のみ。日次実行に含めるか検討 |

### deferred

| タスク | 理由 |
|---|---|
| pytest 導入 | 現在は `test_collect.py` のライブ診断のみ。ユニットテストは投資対効果が低い段階 |
| ログを logging モジュールに移行 | 現在 print ベースで統一されており動作に問題なし。規模拡大時に検討 |
| CSS の外部ファイル化 | `build_site.py` に 300行埋め込み。保守性は低いが動作に支障なし |
| `normalize_items` / `dedupe_articles` の `_extract_links` 統合 | 後処理パイプラインの重複排除であり、抽出ロジックとは責務が異なるため統合不要 |

---

## 9. Next Recommended Tasks

次のエージェントが最初にやるべき作業（優先順）:

1. **`requirements.txt` のバージョン固定** — `pip freeze > requirements.txt` で全依存をピン留め。CI の再現性を確保する。変更量は小さいが効果が大きい。

2. **config.yaml Phase B の検討** — Tier 2 定数（`FETCH_TIMEOUT` の collect_models.py 側、`SKIP_REGIONS` 等）を config.yaml に移行するか判断。必要に応じて実施。

3. **daily-news.yml への model_report 統合検討** — モデルまとめを日次実行に含めるか、週次にするか、引き続き手動のみにするかを決定。API コスト（1回あたり 1 API call）との兼ね合い。

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
