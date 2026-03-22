# HANDOFF.md — AI News System 引き継ぎドキュメント

最終更新: 2026-03-22（第3版）

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
- **テスト用パイプライン** — ペナルティなし全件収集 + モデル比較用 test- ファイル出力
- **メトリクス閲覧** — `python -m scripts.metrics` で収集精度・健全性を確認

---

## 2. Current Status

**フェーズ: 安定運用（拡張可能段階）**

- **日報パイプライン**: 運用中。GitHub Actions で毎日 JST 01:05 に自動実行。
- **モデルまとめ**: 運用可能。GitHub Actions から手動実行（`workflow_dispatch`）。
- **静的サイト**: 運用中。GitHub Pages にデプロイ済み。
- **ソース**: 22ソース / 5リージョン。実効稼働率 91%（arXiv 2本は週末 0件）。
- **安全性修正**: HIGH 5件 + MEDIUM 5件 完了。
- **中期タスク**: 5件すべて完了。
- **要約品質改善**: 4件（RSS フォールバック、スコア基準、system prompt、キーワード拡充）完了。

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
| `scripts/build_site.py` | `python -m scripts.build_site` | 静的サイトのみ再ビルド |
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

### planned

| タスク | 優先度 | 理由 |
|---|---|---|
| ソース別の本文抽出セレクタ（Qiita/Zenn最適化） | **中** | techblog の要約品質向上 |
| クラスタリング判定に summary_ja を追加 | **中** | 重複記事の検知精度向上。閾値調整が必要 |
| model_report 週次自動実行（daily-news.yml に組み込み） | **中** | 手動実行の手間を削減。API コスト +$0.10/週 |
| config.yaml Phase B (Tier 2/3 定数移行) | **低** | Phase A で基盤完成。キーワードリスト等は変更頻度低い |
| `collect.py` の LSP 型エラー修正 | **低** | ランタイムでは問題なし |

### deferred

| タスク | 理由 |
|---|---|
| `fetch_body.py` の JS レンダリングサイト対応 | Playwright 等の導入が必要。依存が大きい |
| pytest 導入 | ライブ診断 + test_pipeline で十分な段階 |
| ログを logging モジュールに移行 | print ベースで統一されており動作に問題なし |
| CSS の外部ファイル化 | `build_site.py` に埋め込み。動作に支障なし |
| 日報の RSS フィード生成 | 需要が発生してから実装 |

---

## 9. Next Recommended Tasks

次のエージェントが最初にやるべき作業（優先順）:

1. **ソース別の本文抽出セレクタ** — `fetch_body.py` にソース名をキーとした優先セレクタ dict を追加。Qiita (`article.it-MdContent`), Zenn (`.znc-article-body`) 等を最適化し、techblog の要約品質を向上。

2. **クラスタリング判定に summary_ja を追加** — `cluster_topics.py` の `tokenize_title` の入力を拡張し、重複記事の検知精度を向上。閾値の調整が必要。

3. **model_report 週次自動実行** — `daily-news.yml` に週1回の model_report 実行を組み込み。手動実行の手間を削減。API コスト +$0.10/週。

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
