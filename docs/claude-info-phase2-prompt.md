# Claude エコシステム情報 Phase 2 — 自動収集パイプライン実装プロンプト

## 概要

Phase 1 で作成した `claude/` ディレクトリ（手動 Markdown + サイト統合）を拡張し、
Claude エコシステムの最新情報を **毎日自動で収集・要約・カテゴリ分類して Markdown に書き出す** パイプラインを構築する。

既存の日報パイプライン（`scripts/main.py`）のアーキテクチャを踏襲しつつ、
**日報形式（日付ごと1ファイル）ではなく、カテゴリ/トピック別に蓄積する形式** とする。

---

## データフロー設計

```
data/claude_feeds.yaml (情報ソース定義)
  → claude_collect.py        ソースから記事を収集（RSS / サイトスクレイピング）
  → claude_seen_urls.py      data/claude_seen_urls.json と照合（URL 重複排除）
  → fetch_body.py            本文取得（既存モジュールを再利用）
  → claude_summarize.py      Claude API で日本語要約 + カテゴリ自動分類 + タグ付与
  → claude_render.py         カテゴリ別 Markdown ファイルへの追記 or 新規生成
  → build_site.py            既存の build_claude_pages() でサイト再ビルド
```

---

## 作成するファイル（新規 6 ファイル）

### 1. `data/claude_feeds.yaml` — ソース定義

既存の `data/feeds.yaml` と同じフォーマットで、Claude エコシステムに特化したソースを定義する。

```yaml
# data/claude_feeds.yaml
# Claude エコシステム情報の収集ソース

official:
  - name: Anthropic News
    type: site
    url: "https://www.anthropic.com/news"
    max_items: 8
    filter_keywords: [claude, anthropic, model, api, safety]

  - name: Anthropic Engineering
    type: rss
    url: "https://www.anthropic.com/engineering/rss.xml"
    max_items: 6

  - name: Claude Code Changelog
    type: site
    url: "https://code.claude.com/docs/en/changelog"
    max_items: 10

  - name: Claude Docs
    type: site
    url: "https://docs.anthropic.com/en/docs/about-claude/models"
    max_items: 5

community:
  - name: Reddit r/ClaudeAI
    type: rss
    url: "https://www.reddit.com/r/ClaudeAI/.rss"
    max_items: 10
    filter_keywords: [claude, code, api, update, release, tip, trick, bug]

  - name: Qiita claude
    type: rss
    url: "https://qiita.com/tags/claude/feed"
    max_items: 6

  - name: Zenn claude
    type: rss
    url: "https://zenn.dev/topics/claude/feed"
    max_items: 6

  - name: Qiita claude-code
    type: rss
    url: "https://qiita.com/tags/claudecode/feed"
    max_items: 6

tools:
  - name: Cursor Forum
    type: rss
    url: "https://forum.cursor.com/latest.rss"
    max_items: 6
    filter_keywords: [claude, anthropic]

  - name: MCP Servers GitHub
    type: site
    url: "https://github.com/anthropics/anthropic-cookbook"
    max_items: 5
```

**設計メモ:**
- `filter_keywords` は新フィールド。記事タイトル/summary に含まれる場合のみ取得するフィルタ
- リージョン概念はなく、`official` / `community` / `tools` のグループで分類
- 各ソースの `max_items` は日報パイプラインより多めに設定（Claude 特化なので関連記事率が高い）

### 2. `data/claude_seen_urls.json` — 重複排除用 URL 履歴

既存の `data/seen_urls.json` と同じ構造。日報パイプラインの URL 履歴とは完全に分離する。

```json
{
  "urls": {},
  "source_penalties": {}
}
```

### 3. `scripts/claude_collect.py` — 収集スクリプト

**参考にすべきファイル:** `scripts/collect.py`

**既存との違い:**
- `data/claude_feeds.yaml` を読み込む（`feeds.yaml` ではない）
- `filter_keywords` による追加フィルタリング: ソース定義にキーワードがある場合、タイトル or summary にキーワードを含む記事のみ取得
- リージョン (`region`) の代わりにグループ (`group`: official / community / tools) をメタデータに付与
- `GOOD_AI_KEYWORDS` の代わりに Claude 特化のキーワードリストを使用

```python
# Claude 関連キーワード（タイトルフィルタ用）
CLAUDE_KEYWORDS = [
    "claude", "anthropic", "claude code", "claude console",
    "sonnet", "opus", "haiku", "mcp", "model context protocol",
    "artifacts", "claude api", "claude desktop",
    "cowork", "cursor", "copilot",  # 比較記事も収集
    "prompt engineering", "プロンプト",
    "claude max", "claude pro", "claude team",
]
```

**入出力:**
- 入力: `data/claude_feeds.yaml`
- 出力: `list[dict]` — 各記事は `{"group", "source", "title", "link", "published", "summary"}` を持つ
- 副出力: `dict[str, int]` — ソース別収集件数（既存パターンと同じ）

**関数シグネチャ:**
```python
def collect_claude_articles() -> tuple[list[dict], dict[str, int]]:
    """Claude 関連の記事を全ソースから収集する。"""
```

**実装上の注意:**
- `scripts/collect.py` の `_request_html()`, `_extract_links()` をインポートして再利用する
- RSS パーシングは `feedparser` を使い、既存と同じ bozo チェックを実施
- `site` タイプのスクレイピングは、既存の `SOURCE_SELECTORS` パターンを参考に、Anthropic / Claude Docs 用のセレクタを定義

### 4. `scripts/claude_summarize.py` — 要約・カテゴリ分類スクリプト

**参考にすべきファイル:** `scripts/summarize.py`

**既存との違い:**
- 要約に加えて、**カテゴリの自動分類** を Claude API に依頼する
- タグ候補は Claude エコシステムに特化したリストを使用
- 重複チェック: 既存の `claude/` ファイル群を読み込み、同一トピックが既にあれば「更新情報」として追記対象にする

**カテゴリ候補:**
```python
CLAUDE_CATEGORIES = [
    "releases",           # リリースノート・アップデート
    "guides",             # セットアップ・使い方
    "tools",              # ツール比較・連携
    "prompts",            # プロンプト関連
    "troubleshooting",    # エラー・問題解決
    "ecosystem",          # 料金・コミュニティ・競合
]
```

**タグ候補:**
```python
CLAUDE_TAG_CANDIDATES = [
    "claude-code", "claude-console", "claude-api",
    "opus", "sonnet", "haiku",
    "mcp", "release", "bugfix", "新機能",
    "setup", "windows", "mac", "linux", "vscode",
    "prompt", "pricing", "performance",
    "cursor", "copilot", "cowork",
]
```

**Claude API プロンプト設計:**

```
あなたは Claude エコシステムの専門情報アナリストです。
以下の記事を分析し、JSON形式で出力してください。

出力フォーマット:
{
  "summary": "日本語で3-5文の要約",
  "category": "releases | guides | tools | prompts | troubleshooting | ecosystem",
  "subcategory": "カテゴリ内の細分類（例: claude-code, claude-api）",
  "tags": ["タグ1", "タグ2", "タグ3"],
  "importance_score": 1-10,
  "is_update_of": "既存記事のファイル名 or null"
}

カテゴリ判定基準:
- releases: 新バージョン、機能追加、API変更、モデルアップデート
- guides: セットアップ手順、使い方Tips、ワークフロー
- tools: ツール比較、MCP サーバー、連携情報
- prompts: プロンプトテンプレート、エンジニアリング技法
- troubleshooting: エラー対処、環境問題、バグ報告
- ecosystem: 料金変更、コミュニティ動向、競合比較

importance_score の基準:
- 9-10: Claude 公式の重大発表（新モデル・大幅な料金変更等）
- 7-8: 公式の機能追加・API変更
- 5-6: 有用な使い方Tips・ツール連携情報
- 3-4: コミュニティの議論・マイナーな Tips
- 1-2: 既知情報の繰り返し・関連性の低い記事
```

**入出力:**
- 入力: `list[dict]` （収集された記事リスト）
- 出力: `list[dict]` — 各記事に `summary_ja`, `category`, `subcategory`, `tags`, `importance_score` が追加された状態

**関数シグネチャ:**
```python
def summarize_claude_articles(articles: list[dict]) -> list[dict]:
    """Claude 関連記事を要約・カテゴリ分類する。"""
```

**実装上の注意:**
- 既存の `summarize.py` の `_safe_parse_summary_json()`, `_clean_json_text()` パターンを踏襲
- API タイムアウトは既存と同じ 120s
- max_tokens は 1000（カテゴリ分類が追加されるため既存より若干大きめ）
- 要約モデルは `claude-sonnet-4-5`（既存と同じ、config.yaml で変更可能に）
- 1記事1 API コール（既存パターンと同じ）

### 5. `scripts/claude_render.py` — Markdown 生成スクリプト

**参考にすべきファイル:** `scripts/render_markdown.py`

**既存との大きな違い:**
- **日付ベースの新規ファイル生成ではなく、カテゴリ別ファイルへの追記**
- 同じカテゴリ+サブカテゴリの記事がすでにあれば、日付セクション（`## YYYY-MM-DD`）として追記
- 新しいサブカテゴリの場合は新規ファイルを作成

**出力先の決定ロジック:**
```
カテゴリ: releases, サブカテゴリ: claude-code
  → claude/releases/claude-code-updates.md（既存ファイルに追記）

カテゴリ: guides, サブカテゴリ: mcp-setup
  → claude/guides/mcp-setup.md（新規作成）

カテゴリ: tools, サブカテゴリ: comparison
  → claude/tools/comparison.md（既存ファイルに追記）
```

**追記の形式:**

既存ファイルに追記する場合、「## 詳細」セクションの直後に日付見出しとして挿入:

```markdown
## 2026-03-24

### 記事タイトル

（要約テキスト）

- **ソース**: [タイトル](URL)
- **重要度**: 7/10
- **タグ**: claude-code, release

---
```

**関数シグネチャ:**
```python
def render_claude_articles(articles: list[dict]) -> list[Path]:
    """要約済み記事をカテゴリ別 Markdown に書き出す。新規作成 or 既存追記。"""
```

**実装上の注意:**
- frontmatter の `updated` フィールドを追記時に更新する
- frontmatter の `sources` リストに新しいソース URL を追加する
- 新規ファイル作成時は `claude/_template.md` のフォーマットに従う
- ファイル名は subcategory をベースに kebab-case で生成（例: `claude-code-updates.md`）
- importance_score が 3 以下の記事は出力しない（ノイズ除去）

### 6. `scripts/claude_main.py` — 統括スクリプト

**参考にすべきファイル:** `scripts/main.py`

```python
"""
claude_main.py — Claude エコシステム情報収集パイプライン

使い方:
  python -m scripts.claude_main

実行フロー:
  1. claude_feeds.yaml からソース定義を読み込み
  2. 各ソースから記事を収集
  3. claude_seen_urls.json と照合（URL 重複排除）
  4. 記事本文を取得（fetch_body.py を再利用）
  5. Claude API で要約 + カテゴリ分類
  6. カテゴリ別 Markdown に書き出し
  7. seen_urls を更新
"""
```

**関数シグネチャ:**
```python
def main():
    # 0. API キー早期チェック
    # 1. 収集
    # 2. 既出URLフィルタ（claude_seen_urls.json）
    # 3. 本文取得（fetch_body.py 再利用）
    # 4. 要約・カテゴリ分類
    # 5. Markdown 書き出し
    # 6. seen_urls 更新
```

**実装上の注意:**
- `scripts/main.py` に一切触れない
- `fetch_body.py` の `fetch_article_bodies()` は直接インポートして再利用
- seen_urls の管理は `scripts/seen_urls.py` のロジックを流用するが、ファイルパスは `data/claude_seen_urls.json` に変更
  - 方法: `claude_seen_urls.py` を新規作成し、`seen_urls.py` の主要関数を import + パスだけ override するラッパーにする。
    あるいは、`seen_urls.py` の `load_seen_data()` 等にオプションのファイルパス引数を追加する（既存動作に影響なし）。後者を推奨
- ペナルティロジックは日報と同じ方式で問題なし

---

## 変更するファイル（既存 3 ファイル）

### 1. `scripts/seen_urls.py` — ファイルパスの柔軟化

**変更内容:** `load_seen_data()`, `update_seen_urls()` 等の関数に `file_path` 引数を追加（デフォルト値は既存の `SEEN_URLS_FILE` のまま）。

```python
# Before
def load_seen_data() -> dict:
    if not SEEN_URLS_FILE.exists():
        ...

# After
def load_seen_data(file_path: Path | None = None) -> dict:
    path = file_path or SEEN_URLS_FILE
    if not path.exists():
        ...
```

**影響範囲:** 既存の呼び出し元（`main.py`, `test_pipeline.py`）は引数なしで呼ぶため、動作は変わらない。

### 2. `.github/workflows/claude-info.yml` — 自動実行ワークフロー（新規）

```yaml
name: Claude Info Update

on:
  workflow_dispatch:
  schedule:
    # JST 07:00 = UTC 22:00（日報とは別の時間帯に実行）
    - cron: "0 22 * * *"

permissions:
  contents: write
  pages: write
  id-token: write

concurrency:
  group: claude-info-main
  cancel-in-progress: true

jobs:
  collect-and-deploy:
    runs-on: ubuntu-latest
    timeout-minutes: 20

    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Sync latest main
        run: |
          git checkout main
          git pull --rebase origin main

      - name: Collect Claude ecosystem info
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          python -m scripts.claude_main

      - name: Commit and push if changed
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

          git add claude/ data/claude_seen_urls.json

          if git diff --cached --quiet; then
            echo "No changes to commit"
          else
            git commit -m "update claude ecosystem info"
            git pull --rebase origin main
            git push origin HEAD:main
          fi

      - name: Build static site
        run: |
          python -m scripts.build_site

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v4
        with:
          path: _site

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**設計ポイント:**
- 実行時間: JST 07:00（日報の JST 01:05 とは6時間ずらし、Pages デプロイの競合を回避）
- `concurrency` グループを日報とは別にする
- コミット対象: `claude/` と `data/claude_seen_urls.json` のみ（日報関連は触らない）

### 3. `docs/HANDOFF.md` — 更新

Phase 2 完了後に以下を更新:
- Section 1 (Overview) に Claude 情報パイプラインのフローを追加
- Section 4 (Key Files) に新規スクリプト群を追加
- Section 5 (Data Flow) に Claude 収集フローの図を追加
- Section 8 (Remaining Roadmap) の planned (Claude エコシステム情報) を done に移動
- Section 7 (Known Caveats) に Claude パイプライン固有のリスクを追加

---

## 制約

- **既存のニュースパイプライン（`scripts/main.py` 等）には一切触れない**
  - 例外: `scripts/seen_urls.py` にオプション引数を追加（既存動作に影響なし）
- **既存のサイト生成ロジックを壊さない**
  - `build_site.py` の Phase 1 で追加した `build_claude_pages()` はそのまま使う。追加の改修は最小限に
- **`fetch_body.py` はインポートして再利用**（コピーしない）
- **API コストを意識**: 記事ごとの要約は max_tokens=1000、importance_score 3 以下はスキップ、1日の最大処理記事数を config.yaml で制御可能にする
- **`data/` にある既存ファイル（`feeds.yaml`, `seen_urls.json`, `metrics.json`）は触らない**
- Claude 情報のデータファイルはすべて `claude_` プレフィックスで命名して分離

---

## config.yaml への追加項目

```yaml
# Claude エコシステム情報パイプライン
claude_max_articles: 20          # 1回の実行で処理する最大記事数
claude_min_importance: 4         # 出力する最低 importance_score
claude_model: "claude-sonnet-4-5"  # 要約に使うモデル
```

---

## 回帰確認

実装後に以下を確認:

### 既存パイプラインの回帰
```bash
# 1. 既存の収集が動くか
python -m scripts.test_collect "TechCrunch"

# 2. サイトビルドが通るか
python -m scripts.build_site

# 3. config 読み込みが動くか
python -c "from scripts.config import get as cfg; print(cfg('model', 'OK'))"

# 4. ペナルティ表示が動くか
python -m scripts.seen_urls

# 5. メトリクス表示が動くか
python -m scripts.metrics
```

### 新パイプラインの確認
```bash
# 6. Claude 収集パイプラインが動くか
python -m scripts.claude_main

# 7. claude/ にファイルが追記/生成されたか
find claude/ -name "*.md" -newer claude/README.md

# 8. サイトに Claude 記事が含まれるか
python -m scripts.build_site
ls _site/claude/

# 9. 検索インデックスに含まれるか
python3 -c "import json; d=json.load(open('_site/search-index.json')); print(len([e for e in d if 'claude/' in e['url']]), 'claude entries')"

# 10. 2回実行しても重複しないか
python -m scripts.claude_main  # 2回目: 新規記事がなければ追記なし
```

---

## 実装順序（推奨）

1. **`data/claude_feeds.yaml`** — ソース定義（これがないと収集できない）
2. **`scripts/seen_urls.py` 修正** — file_path 引数の追加（影響最小、先にやると後続が楽）
3. **`scripts/claude_collect.py`** — 収集ロジック（単体テスト可能）
4. **`scripts/claude_summarize.py`** — 要約・分類（API キーが必要）
5. **`scripts/claude_render.py`** — Markdown 書き出し（4の出力をファイルに書く）
6. **`scripts/claude_main.py`** — 統括（1-5を統合）
7. **`.github/workflows/claude-info.yml`** — 自動化
8. **`docs/HANDOFF.md` 更新** — 引き継ぎ情報の反映
9. **回帰確認** — 上記10項目の実行

各ステップで個別にテスト可能なように、モジュールを疎結合に設計すること。
