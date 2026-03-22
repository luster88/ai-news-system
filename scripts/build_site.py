import json
from pathlib import Path
from datetime import datetime
import html
import re

import markdown
from bs4 import BeautifulSoup

from scripts.metrics import check_health

def _sanitize_dirname(name: str) -> str:
    """ディレクトリ名に使えない文字を除去する（パストラバーサル防止）。"""
    return re.sub(r'[/\\\.\x00]', '_', name).strip('_') or 'unknown'


from scripts.config import get as cfg

BASE_DIR = Path(__file__).resolve().parent.parent
NEWS_DIR = BASE_DIR / "news"
SITE_DIR = BASE_DIR / "_site"
CLAUDE_DIR = BASE_DIR / "claude"

SITE_TITLE = cfg("site_title", "AI News Daily")
PAGE_SIZE = cfg("page_size", 30)  # インデックス1ページあたりの件数


CSS = """
:root{
  --bg:#0b1020;
  --panel:#121933;
  --panel-2:#182142;
  --text:#e8ecff;
  --muted:#aab4df;
  --line:#2a3566;
  --accent:#7aa2ff;
  --accent-2:#9fd3ff;
  --chip:#24315f;
  --chip-tag:#1e3a50;
  --chip-tag-text:#9fd3ff;
  --good:#87e7b0;
  --shadow:0 10px 30px rgba(0,0,0,.25);
}

*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  background:linear-gradient(180deg,#0b1020,#0f1530 40%,#0b1020);
  color:var(--text);
  line-height:1.7;
}
a{color:var(--accent-2);text-decoration:none}
a:hover{text-decoration:underline}
code,pre{
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
.wrap{
  width:min(1100px,calc(100% - 32px));
  margin:0 auto;
}
.header{
  position:sticky; top:0; z-index:20;
  backdrop-filter: blur(12px);
  background:rgba(11,16,32,.75);
  border-bottom:1px solid rgba(255,255,255,.06);
}
.header-inner{
  display:flex; align-items:center; justify-content:space-between;
  gap:12px; padding:12px 0;
  flex-wrap:wrap;
}
.brand{
  font-weight:800; letter-spacing:.2px; font-size:20px;
}
.brand a{color:var(--text); text-decoration:none}
.sub{
  color:var(--muted); font-size:14px;
}
.search-box{
  display:flex; align-items:center; gap:8px;
  flex:1; max-width:340px;
}
.search-box input{
  width:100%;
  background:rgba(255,255,255,.06);
  border:1px solid rgba(255,255,255,.12);
  border-radius:999px;
  color:var(--text);
  padding:7px 14px;
  font-size:14px;
  outline:none;
}
.search-box input::placeholder{color:var(--muted)}
.search-box input:focus{border-color:var(--accent)}
.hero{
  padding:28px 0 8px;
}
.hero-card{
  background:linear-gradient(180deg,var(--panel),var(--panel-2));
  border:1px solid rgba(255,255,255,.06);
  border-radius:20px;
  padding:24px;
  box-shadow:var(--shadow);
}
.hero h1{
  margin:0 0 8px; font-size:34px; line-height:1.15;
}
.hero p{
  margin:0; color:var(--muted);
}
.grid{
  display:grid;
  grid-template-columns: minmax(0, 1.7fr) minmax(280px, .9fr);
  gap:24px;
  padding:24px 0 40px;
}
@media (max-width: 900px){
  .grid{grid-template-columns:1fr}
}
.card{
  background:linear-gradient(180deg,var(--panel),var(--panel-2));
  border:1px solid rgba(255,255,255,.06);
  border-radius:18px;
  padding:20px;
  box-shadow:var(--shadow);
}
.card h2{
  margin:0 0 14px;
  font-size:22px;
}
.list{
  display:grid; gap:14px;
}
.item{
  border:1px solid rgba(255,255,255,.06);
  border-radius:14px;
  padding:16px;
  background:rgba(255,255,255,.02);
}
.item h3{
  margin:0 0 8px; font-size:18px; line-height:1.35;
}
.meta{
  display:flex; flex-wrap:wrap; gap:8px;
  margin-bottom:10px;
}
.chip{
  display:inline-flex; align-items:center;
  border:1px solid rgba(255,255,255,.06);
  background:var(--chip);
  color:var(--muted);
  border-radius:999px;
  padding:4px 10px;
  font-size:12px;
}
.chip-tag{
  display:inline-flex; align-items:center;
  border:1px solid rgba(159,211,255,.2);
  background:var(--chip-tag);
  color:var(--chip-tag-text);
  border-radius:999px;
  padding:4px 10px;
  font-size:12px;
  text-decoration:none;
}
.chip-tag:hover{
  background:#2a4f6e;
  text-decoration:none;
}
.preview{
  color:var(--muted);
  margin:0;
}
.side-list{
  display:grid; gap:10px;
}
.side-list a{
  display:block;
  border:1px solid rgba(255,255,255,.06);
  background:rgba(255,255,255,.02);
  border-radius:12px;
  padding:12px 14px;
}
.tag-cloud{
  display:flex; flex-wrap:wrap; gap:8px;
  margin-top:8px;
}
.pagination{
  display:flex; justify-content:center; gap:10px;
  padding:20px 0;
}
.pagination a, .pagination span{
  display:inline-flex; align-items:center; justify-content:center;
  min-width:40px; height:40px;
  border:1px solid rgba(255,255,255,.12);
  border-radius:10px;
  padding:0 14px;
  font-size:14px;
}
.pagination span.current{
  background:var(--accent);
  color:#0b1020;
  border-color:var(--accent);
  font-weight:700;
}
.footer{
  border-top:1px solid rgba(255,255,255,.06);
  color:var(--muted);
  padding:20px 0 36px;
  font-size:14px;
}
.article{
  padding:24px 0 42px;
}
.article-card{
  background:linear-gradient(180deg,var(--panel),var(--panel-2));
  border:1px solid rgba(255,255,255,.06);
  border-radius:20px;
  padding:28px;
  box-shadow:var(--shadow);
}
.article-header{
  margin-bottom:20px;
  border-bottom:1px solid rgba(255,255,255,.08);
  padding-bottom:18px;
}
.article-title{
  margin:0 0 8px;
  font-size:30px;
  line-height:1.2;
}
.article-meta{
  color:var(--muted);
  font-size:14px;
}
.article-body h1,.article-body h2,.article-body h3{
  margin-top:1.6em;
  line-height:1.25;
}
.article-body h1{font-size:30px}
.article-body h2{font-size:24px}
.article-body h3{font-size:20px}
.article-body p, .article-body li{color:var(--text)}
.article-body ul{padding-left:1.2em}
.article-body hr{
  border:none; border-top:1px solid rgba(255,255,255,.08);
  margin:24px 0;
}
.article-body pre{
  overflow:auto;
  border-radius:14px;
  padding:14px;
  background:#0a0f21;
  border:1px solid rgba(255,255,255,.06);
}
.article-body code{
  background:rgba(255,255,255,.06);
  padding:.18em .38em;
  border-radius:8px;
}
.article-body pre code{
  background:transparent; padding:0;
}
/* テーブル共通 */
.article-body table{
  width:100%;
  max-width:100%;
  border-collapse:collapse;
  margin:16px 0 24px;
  font-size:14px;
  line-height:1.6;
  display:block;
  overflow-x:auto;
  -webkit-overflow-scrolling:touch;
}
.article-body th,
.article-body td{
  padding:10px 14px;
  border:1px solid var(--line);
  text-align:left;
  vertical-align:top;
  overflow-wrap:break-word;
  word-break:break-word;
}
.article-body th{
  background:rgba(255,255,255,.06);
  color:var(--accent-2);
  font-weight:600;
  white-space:nowrap;
}
.article-body tr:hover td{
  background:rgba(255,255,255,.03);
}
/* --- ランキング表 (tbl-ranking) ---
   col1:順位  col2:モデル名  col3:提供元  col4:スコア  col5:備考 */
.tbl-ranking td:nth-child(1){ width:48px; text-align:center; white-space:nowrap; }
.tbl-ranking td:nth-child(2){ min-width:160px; }
.tbl-ranking td:nth-child(3){ white-space:nowrap; }
.tbl-ranking td:nth-child(4){ text-align:right; white-space:nowrap; }
.tbl-ranking td:nth-child(5){ min-width:180px; }
/* --- コスト表 (tbl-pricing) ---
   col1:モデル名  col2:提供元  col3:入力  col4:出力  col5:コスパ */
.tbl-pricing td:nth-child(1){ min-width:140px; }
.tbl-pricing td:nth-child(2){ white-space:nowrap; }
.tbl-pricing td:nth-child(3){ text-align:right; white-space:nowrap; }
.tbl-pricing td:nth-child(4){ text-align:right; white-space:nowrap; }
.tbl-pricing td:nth-child(5){ text-align:center; white-space:nowrap; }
/* --- カテゴリ表 (tbl-category) ---
   col1:モデル名  col2:提供元  col3:リリース日  col4:特徴 */
.tbl-category td:nth-child(1){ min-width:140px; }
.tbl-category td:nth-child(2){ white-space:nowrap; }
.tbl-category td:nth-child(3){ text-align:center; white-space:nowrap; }
.tbl-category td:nth-child(4){ min-width:200px; }
.back{
  margin-bottom:16px;
  display:inline-block;
}
/* 検索結果 */
#search-results .item{ display:none }
#search-results .item.match{ display:block }
#no-results{ display:none; color:var(--muted); padding:20px 0; }
/* details/summary (カテゴリ折りたたみ) */
details.card-toggle summary{
  cursor:pointer; list-style:none; display:flex; align-items:center; gap:8px;
}
details.card-toggle summary::-webkit-details-marker{ display:none; }
details.card-toggle summary::before{
  content:"▶"; font-size:12px; color:var(--muted); transition:transform .2s;
}
details.card-toggle[open] summary::before{ transform:rotate(90deg); }
details.card-toggle summary h2{ margin:0; display:inline; }
details.card-toggle .list{ margin-top:14px; }
/* 日付グループ見出し */
.date-group-heading{
  font-size:16px; font-weight:600; color:var(--accent-2);
  margin:18px 0 8px; padding-bottom:6px;
  border-bottom:1px solid rgba(255,255,255,.08);
}
.date-group-heading:first-child{ margin-top:0; }
"""

SEARCH_JS = """
(function(){
  const input = document.getElementById('search-input');
  if(!input) return;

  let index = null;

  async function loadIndex(){
    try{
      const r = await fetch(ROOT_PATH + '/search-index.json');
      index = await r.json();
    } catch(e){ index = []; }
  }

  function renderResults(q){
    const container = document.getElementById('search-page-results');
    const noResult  = document.getElementById('no-results');
    if(!container) return;

    container.innerHTML = '';
    if(!q || q.length < 2){ noResult.style.display='none'; return; }

    const words = q.toLowerCase().split(/\\s+/).filter(Boolean);
    const hits = (index||[]).filter(item=>{
      const text = (item.title + ' ' + item.summary).toLowerCase();
      return words.every(w => text.includes(w));
    });

    if(hits.length === 0){
      noResult.style.display = 'block';
      return;
    }
    noResult.style.display = 'none';

    hits.slice(0,50).forEach(item=>{
      const div = document.createElement('article');
      div.className = 'item';
      div.innerHTML =
        '<h3><a href="' + ROOT_PATH + '/' + item.url + '">' + escHtml(item.title) + '</a></h3>' +
        '<div class="meta"><span class="chip">' + escHtml(item.date) + '</span></div>' +
        '<p class="preview">' + escHtml((item.summary||'').slice(0,120)) + '</p>';
      container.appendChild(div);
    });
  }

  function escHtml(s){
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  loadIndex().then(()=>{
    const q = new URLSearchParams(location.search).get('q') || '';
    if(q){ input.value = q; renderResults(q); }
  });

  input.addEventListener('input', ()=>{ renderResults(input.value.trim()); });

  // ヘッダーのサーチボックスからページ遷移
  const headerInput = document.getElementById('header-search');
  if(headerInput){
    headerInput.addEventListener('keydown', e=>{
      if(e.key==='Enter' && headerInput.value.trim()){
        location.href = ROOT_PATH + '/search/index.html?q=' + encodeURIComponent(headerInput.value.trim());
      }
    });
  }
})();
"""

MD_EXTENSIONS = [
    "fenced_code",
    "tables",
    "toc",
    "sane_lists",
]


def strip_front_matter(text: str) -> tuple[dict, str]:
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text

    raw_meta, body = parts
    raw_meta = raw_meta.replace("---\n", "", 1)
    meta = {}

    for line in raw_meta.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()

    return meta, body


def _parse_tags_from_meta(meta: dict) -> list[str]:
    """フロントマターの tags フィールドをパースして文字列リストで返す。"""
    raw = meta.get("tags", "")
    if not raw:
        return []
    # "[LLM, Agent, 画像生成]" 形式
    raw = raw.strip().strip("[]")
    return [t.strip() for t in raw.split(",") if t.strip()]


def extract_summary_bullets(md_body: str, max_lines: int = 2) -> list[str]:
    lines = md_body.splitlines()
    bullets = []
    in_summary = False

    for line in lines:
        stripped = line.strip()

        if stripped == "## 今日の総括":
            in_summary = True
            continue

        if in_summary and stripped.startswith("## "):
            break

        if in_summary and stripped.startswith("- "):
            bullets.append(stripped[2:].strip())

        if len(bullets) >= max_lines:
            break

    return bullets


def article_title_from_body(md_body: str, fallback: str) -> str:
    for line in md_body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def read_news_files() -> list[Path]:
    """通常の日報ファイル（prev- / test- を除く）を返す。"""
    return sorted(
        (f for f in NEWS_DIR.glob("*/*/*.md")
         if not f.name.startswith("prev-") and not f.name.startswith("test-")),
        reverse=True,
    )


def read_prev_files() -> list[Path]:
    """prev- プレフィックス付きの保存用ファイルを返す。"""
    return sorted(NEWS_DIR.glob("*/*/*prev-*.md"), reverse=True)


def read_test_files() -> list[Path]:
    """test- プレフィックス付きのテスト出力ファイルを返す。"""
    return sorted(
        (f for f in NEWS_DIR.glob("*/*/*.md") if f.name.startswith("test-")),
        reverse=True,
    )


def page_shell(title: str, body_html: str, root_rel: str = ".") -> str:
    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{root_rel}/style.css">
</head>
<body>
  <header class="header">
    <div class="wrap header-inner">
      <div class="brand"><a href="{root_rel}/index.html">{SITE_TITLE}</a></div>
      <div class="search-box">
        <input id="header-search" type="search" placeholder="記事を検索…" autocomplete="off">
      </div>
      <div class="sub"><a href="{root_rel}/models/index.html" style="color:var(--muted)">モデル一覧</a>
        &nbsp;|&nbsp;
        <a href="{root_rel}/claude/index.html" style="color:var(--muted)">Claude Info</a>
        &nbsp;|&nbsp;
        <a href="{root_rel}/search/index.html" style="color:var(--muted)">検索</a>
        &nbsp;|&nbsp;
        <a href="{root_rel}/tags/index.html" style="color:var(--muted)">タグ一覧</a>
      </div>
    </div>
  </header>
  {body_html}
  <footer class="footer">
    <div class="wrap">Built automatically from daily Markdown files.</div>
  </footer>
  <script>const ROOT_PATH="{root_rel}";</script>
  <script>{SEARCH_JS}</script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# インデックスページ（ページネーション対応）
# ---------------------------------------------------------------------------

def _item_html(file: Path, root_rel: str) -> str:
    rel_parts = file.relative_to(NEWS_DIR).parts
    year, month, filename = rel_parts
    day = filename.replace(".md", "")
    target = f"{root_rel}/news/{year}/{month}/{day}/index.html"

    raw = file.read_text(encoding="utf-8")
    meta, body = strip_front_matter(raw)
    title = article_title_from_body(body, day)
    bullets = extract_summary_bullets(body, max_lines=2)
    preview = " / ".join(html.escape(x) for x in bullets) if bullets else "日報を開く"
    total_items = meta.get("total_items", "")

    tags = _parse_tags_from_meta(meta)
    tags_html = "".join(
        f'<a href="{root_rel}/tags/{html.escape(_sanitize_dirname(t))}/index.html" class="chip-tag">{html.escape(t)}</a>'
        for t in tags
    )
    tags_row = f'<div class="meta" style="margin-top:8px">{tags_html}</div>' if tags_html else ""

    return f"""
    <article class="item">
      <h3><a href="{target}">{html.escape(title)}</a></h3>
      <div class="meta">
        <span class="chip">{html.escape(day)}</span>
        <span class="chip">{html.escape(str(total_items))} items</span>
      </div>
      {tags_row}
      <p class="preview">{preview}</p>
    </article>
    """


def _pagination_html(current_page: int, total_pages: int, root_rel: str) -> str:
    if total_pages <= 1:
        return ""

    parts = []
    if current_page > 1:
        prev_href = f"{root_rel}/index.html" if current_page == 2 else f"{root_rel}/page/{current_page - 1}/index.html"
        parts.append(f'<a href="{prev_href}">← 前</a>')

    for p in range(1, total_pages + 1):
        if p == current_page:
            parts.append(f'<span class="current">{p}</span>')
        else:
            href = f"{root_rel}/index.html" if p == 1 else f"{root_rel}/page/{p}/index.html"
            parts.append(f'<a href="{href}">{p}</a>')

    if current_page < total_pages:
        next_href = f"{root_rel}/page/{current_page + 1}/index.html"
        parts.append(f'<a href="{next_href}">次 →</a>')

    return f'<nav class="pagination">{"".join(parts)}</nav>'


def _build_health_banner() -> str:
    """メトリクスの健全性チェック結果から HTML バナーを生成する。警告なしなら空文字。"""
    try:
        warnings = check_health()
    except Exception:
        return ""

    if not warnings:
        return ""

    zero_sources = [w for w in warnings if w["type"] == "zero_streak"]
    body_warns = [w for w in warnings if w["type"] == "body_rate_low"]
    drop_warns = [w for w in warnings if w["type"] == "count_drop"]

    details = []
    if zero_sources:
        names = ", ".join(w["source"] for w in zero_sources)
        details.append(f"0件が続くソース {len(zero_sources)}件: {names}")
    if body_warns:
        details.append(body_warns[0]["message"])
    if drop_warns:
        details.append(drop_warns[0]["message"])

    detail_html = "<br>".join(html.escape(d) for d in details)

    return f"""
          <div style="background:rgba(255,180,50,.12);border:1px solid rgba(255,180,50,.3);
                      border-radius:12px;padding:14px 18px;margin-top:16px;color:var(--text);font-size:14px">
            <strong style="color:#ffb432">収集健全性: 注意（{len(warnings)}件）</strong><br>
            <span style="color:var(--muted)">{detail_html}</span><br>
            <span style="color:var(--muted);font-size:12px">詳細: python -m scripts.metrics</span>
          </div>"""


def build_index_pages(files: list[Path], prev_files: list[Path] | None = None, test_files: list[Path] | None = None) -> None:
    total_pages = max(1, (len(files) + PAGE_SIZE - 1) // PAGE_SIZE)

    # サイドバーリンク（常に最新14件）
    latest_links = []
    for file in files[:14]:
        rel_parts = file.relative_to(NEWS_DIR).parts
        year, month, filename = rel_parts
        day = filename.replace(".md", "")
        target = f"news/{year}/{month}/{day}/index.html"
        latest_links.append(f'<a href="{target}">{html.escape(day)}</a>')
    side_html = "".join(latest_links) if latest_links else '<div class="preview">まだ日報がありません。</div>'

    # テスト記事リンク
    test_links_html = ""
    if test_files:
        test_links = []
        for file in test_files[:10]:
            rel_parts = file.relative_to(NEWS_DIR).parts
            year, month, filename = rel_parts
            day = filename.replace(".md", "")
            target = f"news/{year}/{month}/{day}/index.html"
            label = day.replace("test-", "")
            test_links.append(f'<a href="{target}">{html.escape(label)}</a>')
        test_links_html = f"""
              <h2 style="margin-top:20px">テスト記事</h2>
              <div class="side-list">
                {"".join(test_links)}
              </div>"""

    # 保存記事リンク
    prev_links_html = ""
    if prev_files:
        prev_links = []
        for file in prev_files[:10]:
            rel_parts = file.relative_to(NEWS_DIR).parts
            year, month, filename = rel_parts
            day = filename.replace(".md", "")
            target = f"news/{year}/{month}/{day}/index.html"
            label = day.replace("prev-", "")
            prev_links.append(f'<a href="{target}">{html.escape(label)} (保存)</a>')
        prev_links_html = f"""
              <h2 style="margin-top:20px">保存記事</h2>
              <div class="side-list">
                {"".join(prev_links)}
              </div>"""

    for page_num in range(1, total_pages + 1):
        start = (page_num - 1) * PAGE_SIZE
        page_files = files[start: start + PAGE_SIZE]

        items_html = [_item_html(f, ".") for f in page_files]

        pagination = _pagination_html(page_num, total_pages, ".")

        health_banner = _build_health_banner() if page_num == 1 else ""

        body_html = f"""
        <main class="wrap">
          <section class="hero">
            <div class="hero-card">
              <h1>{SITE_TITLE}</h1>
              <p>毎日の AI ツール / 企業動向 / 業界ニュースを Markdown から自動で静的サイト化しています。</p>
              {health_banner}
            </div>
          </section>

          <section class="grid">
            <div class="card">
              <h2>{"最新日報" if page_num == 1 else f"{page_num}ページ目"}</h2>
              <div class="list">
                {''.join(items_html) if items_html else '<p class="preview">まだ日報がありません。</p>'}
              </div>
              {pagination}
            </div>

            <aside class="card">
              <h2>最近の日付</h2>
              <div class="side-list">
                {side_html}
              </div>
              {test_links_html}
              {prev_links_html}
            </aside>
          </section>
        </main>
        """

        page_title = SITE_TITLE if page_num == 1 else f"{SITE_TITLE} - {page_num}ページ目"
        html_text = page_shell(page_title, body_html, root_rel=".")

        if page_num == 1:
            (SITE_DIR / "index.html").write_text(html_text, encoding="utf-8")
        else:
            page_dir = SITE_DIR / "page" / str(page_num)
            page_dir.mkdir(parents=True, exist_ok=True)
            (page_dir / "index.html").write_text(html_text, encoding="utf-8")


# ---------------------------------------------------------------------------
# 記事詳細ページ
# ---------------------------------------------------------------------------

def build_article_pages(files: list[Path]) -> None:
    for file in files:
        rel_parts = file.relative_to(NEWS_DIR).parts
        year, month, filename = rel_parts
        day = filename.replace(".md", "")

        raw = file.read_text(encoding="utf-8")
        meta, body = strip_front_matter(raw)
        title = article_title_from_body(body, day)

        article_html = markdown.markdown(body, extensions=MD_EXTENSIONS)

        out_dir = SITE_DIR / "news" / year / month / day
        out_dir.mkdir(parents=True, exist_ok=True)

        tags = _parse_tags_from_meta(meta)
        tags_html = "".join(
            f'<a href="../../../../tags/{html.escape(_sanitize_dirname(t))}/index.html" class="chip-tag">{html.escape(t)}</a>'
            for t in tags
        )
        tags_row = f'<div class="meta" style="margin-top:10px">{tags_html}</div>' if tags_html else ""

        body_html = f"""
        <main class="wrap article">
          <a class="back" href="../../../../index.html">← index に戻る</a>
          <article class="article-card">
            <div class="article-header">
              <h1 class="article-title">{html.escape(title)}</h1>
              <div class="article-meta">
                date: {html.escape(meta.get('date', day))} / total_items: {html.escape(meta.get('total_items', ''))}
              </div>
              {tags_row}
            </div>
            <div class="article-body">
              {article_html}
            </div>
          </article>
        </main>
        """

        html_text = page_shell(title, body_html, root_rel="../../../../")
        (out_dir / "index.html").write_text(html_text, encoding="utf-8")


# ---------------------------------------------------------------------------
# タグページ
# ---------------------------------------------------------------------------

def build_tag_pages(files: list[Path]) -> None:
    """タグ別記事一覧ページを _site/tags/{タグ名}/index.html に生成する。"""
    tag_to_files: dict[str, list[Path]] = {}

    for file in files:
        raw = file.read_text(encoding="utf-8")
        meta, _ = strip_front_matter(raw)
        for tag in _parse_tags_from_meta(meta):
            tag_to_files.setdefault(tag, []).append(file)

    # 全タグ一覧ページ
    tags_dir = SITE_DIR / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)

    tag_links = "".join(
        f'<a href="{html.escape(_sanitize_dirname(tag))}/index.html" class="chip-tag">'
        f'{html.escape(tag)} ({len(flist)})</a>'
        for tag, flist in sorted(tag_to_files.items())
    )
    overview_body = f"""
    <main class="wrap">
      <section class="hero">
        <div class="hero-card">
          <h1>タグ一覧</h1>
          <p>記事に付与されたカテゴリタグの一覧です。</p>
        </div>
      </section>
      <section style="padding:24px 0">
        <div class="card">
          <h2>すべてのタグ</h2>
          <div class="tag-cloud">
            {tag_links if tag_links else '<p class="preview">タグがありません。</p>'}
          </div>
        </div>
      </section>
    </main>
    """
    (tags_dir / "index.html").write_text(
        page_shell("タグ一覧 - " + SITE_TITLE, overview_body, root_rel=".."),
        encoding="utf-8",
    )

    # 各タグの記事一覧ページ
    for tag, tag_files in tag_to_files.items():
        items_html = [_item_html(f, "../..") for f in tag_files]

        body_html = f"""
        <main class="wrap">
          <section class="hero">
            <div class="hero-card">
              <h1>タグ: {html.escape(tag)}</h1>
              <p>{len(tag_files)} 件の記事があります。</p>
            </div>
          </section>
          <section style="padding:24px 0 40px">
            <div class="card">
              <h2>{html.escape(tag)}</h2>
              <div class="list">
                {''.join(items_html)}
              </div>
            </div>
          </section>
        </main>
        """

        tag_dir = tags_dir / _sanitize_dirname(tag)
        tag_dir.mkdir(parents=True, exist_ok=True)
        (tag_dir / "index.html").write_text(
            page_shell(f"{tag} - {SITE_TITLE}", body_html, root_rel="../.."),
            encoding="utf-8",
        )


# ---------------------------------------------------------------------------
# 検索インデックス & 検索ページ
# ---------------------------------------------------------------------------

def build_search_index(files: list[Path]) -> None:
    """_site/search-index.json を生成する。"""
    entries = []

    for file in files:
        rel_parts = file.relative_to(NEWS_DIR).parts
        year, month, filename = rel_parts
        day = filename.replace(".md", "")

        raw = file.read_text(encoding="utf-8")
        meta, body = strip_front_matter(raw)
        title = article_title_from_body(body, day)
        bullets = extract_summary_bullets(body, max_lines=3)
        summary = " ".join(bullets)

        entries.append({
            "date": day,
            "title": title,
            "summary": summary,
            "url": f"news/{year}/{month}/{day}/index.html",
            "tags": _parse_tags_from_meta(meta),
        })

    # Claude 記事も検索インデックスに含める
    entries.extend(_collect_claude_search_entries())

    (SITE_DIR / "search-index.json").write_text(
        json.dumps(entries, ensure_ascii=False, indent=None),
        encoding="utf-8",
    )


def build_search_page() -> None:
    """_site/search/index.html を生成する。"""
    search_dir = SITE_DIR / "search"
    search_dir.mkdir(parents=True, exist_ok=True)

    body_html = """
    <main class="wrap">
      <section class="hero">
        <div class="hero-card">
          <h1>記事検索</h1>
          <p>タイトル・要約のキーワードで絞り込みます。</p>
        </div>
      </section>
      <section style="padding:24px 0 40px">
        <div class="card">
          <input id="search-input" type="search"
            placeholder="キーワードを入力…"
            style="width:100%;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
                   border-radius:12px;color:var(--text);padding:10px 16px;font-size:16px;
                   outline:none;margin-bottom:20px;">
          <div id="no-results" style="color:var(--muted)">該当する記事が見つかりませんでした。</div>
          <div id="search-page-results" class="list"></div>
        </div>
      </section>
    </main>
    """

    (search_dir / "index.html").write_text(
        page_shell("記事検索 - " + SITE_TITLE, body_html, root_rel=".."),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# モデルまとめページ
# ---------------------------------------------------------------------------

MODELS_DIR = BASE_DIR / "models"

# テーブル分類: ヘッダーに含まれるキーワード → CSS クラス
_TABLE_CLASS_RULES = [
    (["順位"], "tbl-ranking"),
    (["入力", "出力", "コスパ"], "tbl-pricing"),
    (["リリース日"], "tbl-category"),
]


def _classify_model_tables(html_text: str) -> str:
    """テーブルの <thead> 内容を見て CSS クラスを付与する。"""
    soup = BeautifulSoup(html_text, "lxml")

    for table in soup.find_all("table"):
        header_text = ""
        thead = table.find("thead")
        if thead:
            header_text = thead.get_text(" ", strip=True)

        cls = "tbl-category"  # デフォルト
        for keywords, class_name in _TABLE_CLASS_RULES:
            if all(kw in header_text for kw in keywords):
                cls = class_name
                break

        table["class"] = table.get("class", []) + [cls]

    # BeautifulSoup が追加する html/body タグを除去して中身だけ返す
    body = soup.find("body")
    return body.decode_contents() if body else str(soup)


def _render_model_md_to_html(md_path: Path, back_href: str, back_label: str, root_rel: str, history_links_html: str = "") -> str:
    """モデルまとめ Markdown を HTML ページ文字列に変換する共通ヘルパー。"""
    raw = md_path.read_text(encoding="utf-8")
    meta, body = strip_front_matter(raw)
    report_date = meta.get("date", "")
    title = article_title_from_body(body, "最新AIモデルまとめ")

    raw_html = markdown.markdown(body, extensions=MD_EXTENSIONS)
    article_html = _classify_model_tables(raw_html)

    date_note = f"（{html.escape(report_date)} 時点の情報）" if report_date else ""

    body_html = f"""
    <main class="wrap article model-report">
      <a class="back" href="{back_href}">{back_label}</a>
      <article class="article-card">
        <div class="article-header">
          <h1 class="article-title">{html.escape(title)}</h1>
          <div class="article-meta">
            最終更新: {html.escape(report_date)} {date_note}
          </div>
        </div>
        <div class="article-body">
          {article_html}
        </div>
      </article>
      {history_links_html}
    </main>
    """

    return page_shell(title, body_html, root_rel=root_rel)


def build_model_page() -> None:
    """models/latest.md と models/history/*.md を HTML 化する。"""
    latest_md = MODELS_DIR / "latest.md"
    if not latest_md.exists():
        print("[info] models/latest.md not found, skipping model page")
        return

    out_dir = SITE_DIR / "models"
    out_dir.mkdir(parents=True, exist_ok=True)

    # history ファイルを収集（新しい順）
    history_dir = MODELS_DIR / "history"
    history_files = sorted(history_dir.glob("*.md"), reverse=True) if history_dir.exists() else []

    # 過去レポート一覧 HTML
    history_links = ""
    if history_files:
        links = []
        for hf in history_files:
            date_str = hf.stem
            links.append(
                f'<a href="history/{html.escape(date_str)}/index.html" '
                f'class="chip-tag">{html.escape(date_str)}</a>'
            )
        history_links = f"""
      <div class="card" style="margin-top:24px">
        <h2>過去のレポート</h2>
        <div class="tag-cloud">
          {"".join(links)}
        </div>
      </div>"""

    # latest ページ生成
    html_text = _render_model_md_to_html(
        latest_md,
        back_href="../index.html",
        back_label="← index に戻る",
        root_rel="..",
        history_links_html=history_links,
    )
    (out_dir / "index.html").write_text(html_text, encoding="utf-8")
    print(f"[info] built model page: {out_dir / 'index.html'}")

    # history 各ページ生成
    hist_out_dir = out_dir / "history"
    for hf in history_files:
        date_str = hf.stem
        page_dir = hist_out_dir / date_str
        page_dir.mkdir(parents=True, exist_ok=True)

        html_text = _render_model_md_to_html(
            hf,
            back_href="../../index.html",
            back_label="← 最新のモデルまとめに戻る",
            root_rel="../../..",
        )
        (page_dir / "index.html").write_text(html_text, encoding="utf-8")

    if history_files:
        print(f"[info] built {len(history_files)} model history page(s)")


# ---------------------------------------------------------------------------
# Claude エコシステム情報ページ
# ---------------------------------------------------------------------------

# カテゴリ定義 (ディレクトリ名, 表示名, 概要説明)
_CLAUDE_CATEGORIES = [
    ("releases",        "リリース情報",           "モデル・Claude Code・Console・API のアップデート情報"),
    ("guides",          "ガイド",                 "セットアップ手順・ワークフロー・ベストプラクティス"),
    ("tools",           "ツール比較",             "関連ツール比較・MCP サーバー・IDE 連携情報"),
    ("prompts",         "プロンプト",             "プロンプトテンプレート・エンジニアリング技法"),
    ("troubleshooting", "トラブルシューティング",   "よくあるエラーと対処法・環境別の問題"),
    ("ecosystem",       "エコシステム",            "料金・プラン・コミュニティ動向・競合比較"),
]

# カテゴリ名の逆引き辞書
_CLAUDE_CAT_LABELS = {d: l for d, l, _ in _CLAUDE_CATEGORIES}


def _read_claude_articles() -> list[tuple[str, str, Path]]:
    """claude/ 配下の Markdown ファイルを (category, slug, path) のリストで返す。
    _template.md と README.md は除外する。"""
    if not CLAUDE_DIR.exists():
        return []

    articles = []
    for cat_dir, _, _ in _CLAUDE_CATEGORIES:
        cat_path = CLAUDE_DIR / cat_dir
        if not cat_path.is_dir():
            continue
        for md_file in sorted(cat_path.glob("*.md"), reverse=True):
            if md_file.name.startswith("_"):
                continue
            slug = md_file.stem
            articles.append((cat_dir, slug, md_file))

    return articles


def _claude_summary_from_body(body: str) -> str:
    """Markdown 本文から概要テキストを抽出する（見出し・区切り・テーブル・リスト行を除く）。"""
    lines = []
    for l in body.splitlines():
        s = l.strip()
        if not s:
            continue
        if s.startswith(("#", "---", "|", "- ", "* ", "```")):
            continue
        lines.append(s)
        if len(lines) >= 2:
            break
    text = " ".join(lines)[:120]
    # Markdown 記法を除去
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text


def _claude_article_item(category: str, slug: str, meta: dict, title: str, root_rel: str,
                          summary: str = "") -> str:
    """Claude 記事の一覧アイテム HTML を返す。"""
    target = f"{root_rel}/claude/{category}/{slug}/index.html"
    date_str = meta.get("date", "")
    tags = _parse_tags_from_meta(meta)
    tags_html = "".join(
        f'<span class="chip-tag">{html.escape(t)}</span>'
        for t in tags[:5]
    )
    summary_html = f'<p class="preview" style="margin:4px 0 0;font-size:14px">{html.escape(summary)}</p>' if summary else ''

    return f"""
    <article class="item">
      <h3><a href="{target}">{html.escape(title)}</a></h3>
      <div class="meta">
        <span class="chip">{html.escape(date_str)}</span>
        <span class="chip">{html.escape(category)}</span>
      </div>
      {summary_html}
      {f'<div class="meta">{tags_html}</div>' if tags_html else ''}
    </article>
    """


def _rewrite_claude_md_links(html_text: str) -> str:
    """Claude 記事 HTML 内の .md 相対リンクを生成後の HTML パスに変換する。

    Markdown ソースでは ``../category/slug.md`` と記述するが、
    生成先は ``_site/claude/{cat}/{slug}/index.html`` で1段深いため、
    ``../../category/slug/index.html`` に書き換える必要がある。
    """
    # ../category/slug.md → ../../category/slug/index.html
    html_text = re.sub(
        r'href="\.\./([^/]+)/([^"]+)\.md"',
        r'href="../../\1/\2/index.html"',
        html_text,
    )
    # ../README.md → ../../index.html
    html_text = re.sub(
        r'href="\.\./README\.md"',
        r'href="../../index.html"',
        html_text,
    )
    return html_text


def build_claude_pages() -> None:
    """claude/ 配下の Markdown を _site/claude/ に HTML 化する。"""
    articles = _read_claude_articles()
    if not articles:
        print("[info] no claude articles found, skipping claude pages")
        return

    out_base = SITE_DIR / "claude"
    out_base.mkdir(parents=True, exist_ok=True)

    # --- カテゴリ別集計 ---
    cat_counts: dict[str, int] = {}
    for cat, _, _ in articles:
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    # --- カテゴリ概要カード HTML ---
    cat_cards_html = []
    for cat_dir, cat_label, cat_desc in _CLAUDE_CATEGORIES:
        cnt = cat_counts.get(cat_dir, 0)
        if cnt > 0:
            count_badge = f'{cnt} 件'
            link = f'<a href="category/{cat_dir}/index.html" style="color:var(--accent-2);font-size:13px">記事を見る →</a>'
        else:
            count_badge = '準備中'
            link = ''
        cat_cards_html.append(f"""
          <div class="item" style="display:flex;flex-direction:column;gap:6px">
            <div style="display:flex;align-items:center;justify-content:space-between;gap:8px">
              <h3 style="margin:0;font-size:17px">{html.escape(cat_label)}</h3>
              <span class="chip" style="font-size:11px">{count_badge}</span>
            </div>
            <p class="preview" style="margin:0;font-size:14px">{html.escape(cat_desc)}</p>
            {link}
          </div>""")

    # --- サイドナビ HTML（全カテゴリ表示） ---
    side_links = []
    for cat_dir, cat_label, _ in _CLAUDE_CATEGORIES:
        cnt = cat_counts.get(cat_dir, 0)
        label = f'{html.escape(cat_label)} ({cnt})' if cnt > 0 else f'{html.escape(cat_label)}'
        side_links.append(
            f'<a href="category/{cat_dir}/index.html">{label}</a>'
        )
    side_nav_html = "".join(side_links)

    # --- インデックスページ (_site/claude/index.html) ---
    # 記事データを収集し日付でグループ化
    article_entries: list[tuple[str, str]] = []  # (date, item_html)
    for cat, slug, md_file in articles:
        raw = md_file.read_text(encoding="utf-8")
        meta, body = strip_front_matter(raw)
        title = article_title_from_body(body, slug)
        summary = _claude_summary_from_body(body)
        date_str = str(meta.get("date", "")).strip("'")
        item_html = _claude_article_item(cat, slug, meta, title, "..", summary=summary)
        article_entries.append((date_str, item_html))

    # 日付降順でソート → グループ化
    article_entries.sort(key=lambda x: x[0], reverse=True)
    grouped_html_parts: list[str] = []
    current_date = ""
    for date_str, item_html in article_entries:
        if date_str != current_date:
            current_date = date_str
            count = sum(1 for d, _ in article_entries if d == date_str)
            grouped_html_parts.append(
                f'<div class="date-group-heading">{html.escape(date_str)}（{count}件）</div>'
            )
        grouped_html_parts.append(item_html)
    articles_section = "".join(grouped_html_parts) if grouped_html_parts else '<p class="preview">記事がありません。</p>'

    body_html = f"""
    <main class="wrap">
      <section class="hero">
        <div class="hero-card">
          <h1>Claude エコシステム情報</h1>
          <p>Claude / Claude Code / Claude Console および関連ツールの最新情報をカテゴリ別に整理しています。</p>
        </div>
      </section>
      <section style="padding:20px 0 0">
        <div class="card">
          <details class="card-toggle">
            <summary><h2>カテゴリ一覧</h2></summary>
            <div class="list" style="grid-template-columns:repeat(auto-fill,minmax(280px,1fr))">
              {''.join(cat_cards_html)}
            </div>
          </details>
        </div>
      </section>
      <section class="grid">
        <div class="card">
          <h2>すべての記事</h2>
          <div class="list">
            {articles_section}
          </div>
        </div>
        <aside class="card">
          <h2>カテゴリ</h2>
          <div class="side-list">
            {side_nav_html}
          </div>
        </aside>
      </section>
    </main>
    """
    (out_base / "index.html").write_text(
        page_shell("Claude エコシステム情報 - " + SITE_TITLE, body_html, root_rel=".."),
        encoding="utf-8",
    )

    # --- カテゴリ別一覧ページ (_site/claude/category/{cat}/index.html) ---
    for cat_dir, cat_label, _ in _CLAUDE_CATEGORIES:
        cat_articles = [(c, s, p) for c, s, p in articles if c == cat_dir]
        if not cat_articles:
            continue

        items_html = []
        for cat, slug, md_file in cat_articles:
            raw = md_file.read_text(encoding="utf-8")
            meta, body = strip_front_matter(raw)
            title = article_title_from_body(body, slug)
            summary = _claude_summary_from_body(body)
            items_html.append(_claude_article_item(cat, slug, meta, title, "../../..", summary=summary))

        cat_body = f"""
        <main class="wrap">
          <section class="hero">
            <div class="hero-card">
              <h1>{html.escape(cat_label)}</h1>
              <p>{len(cat_articles)} 件の記事があります。</p>
            </div>
          </section>
          <section style="padding:24px 0 40px">
            <div class="card">
              <a class="back" href="../../index.html" style="display:inline-block;margin-bottom:16px">← Claude Info に戻る</a>
              <h2>{html.escape(cat_label)}</h2>
              <div class="list">
                {''.join(items_html)}
              </div>
            </div>
          </section>
        </main>
        """

        cat_out = out_base / "category" / cat_dir
        cat_out.mkdir(parents=True, exist_ok=True)
        (cat_out / "index.html").write_text(
            page_shell(f"{cat_label} - Claude Info - {SITE_TITLE}", cat_body, root_rel="../../.."),
            encoding="utf-8",
        )

    # --- 個別記事ページ (_site/claude/{category}/{slug}/index.html) ---
    article_count = 0
    for cat, slug, md_file in articles:
        raw = md_file.read_text(encoding="utf-8")
        meta, body = strip_front_matter(raw)
        title = article_title_from_body(body, slug)

        article_html = markdown.markdown(body, extensions=MD_EXTENSIONS)
        article_html = _rewrite_claude_md_links(article_html)
        updated = meta.get("updated", meta.get("date", ""))
        cat_label = _CLAUDE_CAT_LABELS.get(cat, cat)

        tags = _parse_tags_from_meta(meta)
        tags_html = "".join(
            f'<span class="chip-tag">{html.escape(t)}</span>'
            for t in tags
        )
        tags_row = f'<div class="meta" style="margin-top:10px">{tags_html}</div>' if tags_html else ""

        detail_body = f"""
        <main class="wrap article">
          <a class="back" href="../../index.html">← Claude Info に戻る</a>
          <article class="article-card">
            <div class="article-header">
              <h1 class="article-title">{html.escape(title)}</h1>
              <div class="article-meta">
                カテゴリ: {html.escape(cat_label)} / 最終更新: {html.escape(updated)}
              </div>
              {tags_row}
            </div>
            <div class="article-body">
              {article_html}
            </div>
          </article>
        </main>
        """

        art_out = out_base / cat / slug
        art_out.mkdir(parents=True, exist_ok=True)
        (art_out / "index.html").write_text(
            page_shell(f"{title} - Claude Info - {SITE_TITLE}", detail_body, root_rel="../../.."),
            encoding="utf-8",
        )
        article_count += 1

    print(f"[info] built claude pages: {article_count} article(s), {len([c for c in cat_counts if cat_counts[c] > 0])} category page(s)")


def _collect_claude_search_entries() -> list[dict]:
    """Claude 記事の検索インデックスエントリを返す。"""
    articles = _read_claude_articles()
    entries = []

    for cat, slug, md_file in articles:
        raw = md_file.read_text(encoding="utf-8")
        meta, body = strip_front_matter(raw)
        title = article_title_from_body(body, slug)

        # 本文から最初の数行を summary として抽出
        lines = [l.strip() for l in body.splitlines()
                 if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("---")]
        summary = " ".join(lines[:3])[:200]

        entries.append({
            "date": meta.get("date", ""),
            "title": title,
            "summary": summary,
            "url": f"claude/{cat}/{slug}/index.html",
            "tags": _parse_tags_from_meta(meta),
        })

    return entries


# ---------------------------------------------------------------------------
# エントリポイント
# ---------------------------------------------------------------------------

def main():
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "style.css").write_text(CSS, encoding="utf-8")
    (SITE_DIR / ".nojekyll").write_text("", encoding="utf-8")

    files = read_news_files()
    prev_files = read_prev_files()
    test_files = read_test_files()
    all_files = files + prev_files + test_files

    build_index_pages(files, prev_files=prev_files, test_files=test_files)
    build_article_pages(all_files)
    build_tag_pages(all_files)
    build_search_index(all_files)
    build_search_page()
    build_model_page()
    build_claude_pages()

    print(f"[info] built site: {SITE_DIR}")
    print(f"[info]   {len(files)} articles, {len(prev_files)} prev articles, {max(1, (len(files) + PAGE_SIZE - 1) // PAGE_SIZE)} index page(s)")


if __name__ == "__main__":
    main()
