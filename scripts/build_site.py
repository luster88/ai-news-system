import json
from pathlib import Path
from datetime import datetime
import html
import re

import markdown
import yaml
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
/* ===== Linear-style Design System ===== */
:root{
  --bg:#1e1e2e;
  --surface:#161625;
  --surface-hover:#252538;
  --surface-active:#2e2e42;
  --text-primary:#d4d4d4;
  --text-secondary:#9a9ab0;
  --text-tertiary:#6c6c80;
  --text-heading:#ffffff;
  --border:rgba(255,255,255,.08);
  --accent:#7b8fff;
  --accent-hover:#7eb8f7;
  --accent-dim:rgba(123,143,255,.18);
}

*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  background:var(--bg);
  color:var(--text-primary);
  line-height:1.5;
  font-size:14px;
}
a{color:var(--text-primary);text-decoration:none}
a:hover{color:var(--accent-hover)}
code,pre{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}

/* --- App Shell --- */
.app{display:flex;flex-direction:column;height:100vh}
.topbar{
  display:flex;align-items:center;gap:16px;
  padding:0 20px;height:44px;min-height:44px;
  background:var(--surface);
  border-bottom:1px solid var(--border);
  position:sticky;top:0;z-index:50;
}
.topbar-brand{font-weight:600;font-size:14px;white-space:nowrap}
.topbar-brand a{color:var(--text-heading)}
.topbar-nav{display:flex;align-items:center;gap:2px;margin-left:8px}
.topbar-nav a{
  padding:4px 10px;border-radius:4px;
  font-size:13px;color:var(--text-secondary);
  transition:background .12s,color .12s;
}
.topbar-nav a:hover{background:var(--surface-hover);color:var(--text-heading)}
.topbar-nav a.active{background:var(--accent-dim);color:var(--accent)}
.topbar-search{
  margin-left:auto;
  position:relative;
}
.topbar-search input{
  width:200px;
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:6px;
  color:var(--text-primary);
  padding:5px 10px 5px 28px;
  font-size:13px;outline:none;
  transition:border-color .15s,width .2s;
}
.topbar-search input:focus{border-color:var(--accent);width:280px}
.topbar-search input::placeholder{color:var(--text-tertiary)}
.topbar-search::before{
  content:"⌘K";position:absolute;right:8px;top:50%;transform:translateY(-50%);
  font-size:11px;color:var(--text-tertiary);pointer-events:none;
}
/* Mobile menu toggle */
.mobile-menu-btn{
  display:none;width:32px;height:32px;
  align-items:center;justify-content:center;
  background:none;border:none;color:var(--text-secondary);
  font-size:18px;cursor:pointer;border-radius:4px;
  transition:background .12s;
}
.mobile-menu-btn:hover{background:var(--surface-hover)}

/* --- 3-Column Layout --- */
.layout{display:flex;flex:1;overflow:hidden}
.sidebar-left{
  width:200px;min-width:200px;
  background:var(--surface);
  border-right:1px solid var(--border);
  overflow-y:auto;
  padding:12px 0;
}
.content-area{flex:1;overflow-y:auto;padding:0}
.content-area>.content-header,
.content-area>.list-view,
.content-area>.pagination,
.content-area>.cat-grid{max-width:860px;margin-left:auto;margin-right:auto}
.content-area>div[style]{max-width:860px;margin-left:auto;margin-right:auto}
.sidebar-right{
  width:220px;min-width:220px;
  background:var(--surface);
  border-left:1px solid var(--border);
  overflow-y:auto;
  padding:16px;
}

/* --- Responsive --- */
@media(max-width:1200px){.sidebar-right{display:none}}
@media(max-width:800px){
  .sidebar-left{
    display:none;position:fixed;left:0;top:44px;bottom:0;z-index:40;
    width:260px;
  }
  .sidebar-left.open{display:block}
  .mobile-menu-btn{display:flex}
  .topbar-nav a{padding:4px 8px;font-size:12px}
  .topbar-search{display:none}
  .topbar{padding:0 12px;gap:8px}
  .content-header{padding:12px 16px 0 !important}
  .list-row{padding:12px 16px 14px !important}
  .date-group-heading{padding:10px 16px 4px !important}
  .month-tabs{margin-top:8px}
  .month-tab{padding:5px 10px;font-size:11px}
  .article-detail{padding:20px 16px !important}
  .footer{padding:10px 16px}
}

/* --- Sidebar Navigation --- */
.side-section{padding:0 10px;margin-bottom:16px}
.side-heading{
  font-size:10px;font-weight:600;text-transform:uppercase;
  letter-spacing:.6px;color:var(--text-tertiary);
  padding:8px 8px 6px;
}
.side-link{
  display:flex;align-items:center;gap:6px;
  padding:4px 8px;border-radius:4px;
  font-size:12px;color:var(--text-secondary);
  transition:background .12s,color .12s;
  cursor:pointer;
}
.side-link:hover{background:var(--surface-hover);color:var(--text-heading)}
.side-link.active{background:var(--accent-dim);color:var(--accent)}
.side-count{
  margin-left:auto;font-size:10px;color:var(--text-tertiary);
}
/* --- Sidebar Tree (year/month collapsible) --- */
.side-tree{padding:0 10px;margin-bottom:16px}
.side-tree details{margin:0}
.side-tree summary{
  list-style:none;cursor:pointer;
  display:flex;align-items:center;gap:4px;
  padding:3px 8px;border-radius:4px;
  transition:background .12s;
  user-select:none;
}
.side-tree summary::-webkit-details-marker{display:none}
.side-tree summary:hover{background:var(--surface-hover)}
.side-tree summary::before{
  content:"▸";font-size:9px;color:var(--text-tertiary);
  width:10px;text-align:center;flex-shrink:0;
  transition:transform .15s;
}
.side-tree details[open]>summary::before{transform:rotate(90deg)}
.side-tree .tree-year>summary{
  font-size:11px;font-weight:600;color:var(--text-tertiary);
  padding:6px 8px 4px;
  letter-spacing:.3px;
}
.side-tree .tree-month>summary{
  font-size:11px;font-weight:500;color:var(--text-secondary);
  padding:3px 8px 3px 18px;
}
.side-tree .tree-month .side-link{
  padding-left:28px;font-size:11px;
}
.side-tree .tree-month .side-count{font-size:9px}

/* --- Content Header --- */
.content-header{
  padding:16px 28px 0;
  border-bottom:1px solid var(--border);
}
.content-title{font-size:15px;font-weight:600;color:var(--text-heading)}
.content-subtitle{font-size:12px;color:var(--text-tertiary);margin-top:2px}
/* Month tabs */
.month-tabs{
  display:flex;gap:0;margin-top:10px;overflow-x:auto;
  -webkit-overflow-scrolling:touch;
}
.month-tab{
  padding:6px 14px;font-size:12px;
  color:var(--text-tertiary);white-space:nowrap;
  border-bottom:2px solid transparent;
  transition:color .12s,border-color .12s;
  cursor:pointer;text-decoration:none;
}
.month-tab:hover{color:var(--text-primary)}
.month-tab.active{
  color:var(--accent);
  border-bottom-color:var(--accent);
}

/* --- List Items --- */
.list-view{padding:0}
.list-row{
  display:block;
  padding:14px 28px 16px;
  border-bottom:1px solid var(--border);
  transition:background .15s;
  cursor:pointer;
  text-decoration:none;
  color:inherit;
}
.list-row:hover{background:var(--surface-hover)}
.list-row:active{background:var(--surface-active)}
.list-row:first-child{border-top:none}
/* 最新の記事を少しだけ強調 */
.list-row:first-child .list-row-title{color:var(--text-heading)}
.list-row:first-child .list-row-title::before{
  content:"";display:inline-block;width:6px;height:6px;
  background:var(--accent);border-radius:50%;
  margin-right:8px;vertical-align:middle;
  position:relative;top:-1px;
}
.list-row-body{min-width:0}
.list-row-title{
  font-size:15px;font-weight:600;
  color:var(--text-primary);
  line-height:1.45;
  margin-bottom:4px;
}
.list-row-summary{
  font-size:13px;color:var(--text-secondary);
  line-height:1.55;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;
}
.list-row-meta{
  display:flex;align-items:center;gap:8px;
  margin-top:8px;
}
.meta-date{
  font-size:11px;color:var(--text-tertiary);white-space:nowrap;
}
.meta-count{
  font-size:11px;color:var(--text-tertiary);white-space:nowrap;
}
.meta-count::after{content:" items"}

/* --- Tags --- */
.tag{
  display:inline-block;
  background:#2a2a3e;
  color:#a0a0c0;
  padding:1px 6px;border-radius:3px;
  font-size:11px;line-height:1.5;
  text-decoration:none;
  transition:color .12s,background .12s;
}
.tag:hover{color:var(--text-primary);background:#353550}
.tag+.tag{margin-left:4px}
.tag-row{display:inline-flex;flex-wrap:wrap;align-items:center;margin-left:4px}

/* --- Date Group --- */
.date-group-heading{
  font-size:11px;font-weight:600;text-transform:uppercase;
  letter-spacing:.3px;color:var(--text-tertiary);
  padding:12px 28px 6px;
  background:var(--bg);
  position:sticky;top:0;z-index:5;
}

/* --- Pagination --- */
.pagination{
  display:flex;align-items:center;justify-content:center;gap:4px;
  padding:16px 24px;border-top:1px solid var(--border);
}
.pagination a,.pagination span{
  display:inline-flex;align-items:center;justify-content:center;
  min-width:32px;height:28px;
  border-radius:4px;padding:0 8px;font-size:13px;
  color:var(--text-secondary);
  transition:background .12s;
}
.pagination a:hover{background:var(--surface-hover);color:var(--text-heading)}
.pagination .current{background:var(--accent-dim);color:var(--accent);font-weight:600}

/* --- Sidebar Right Sections --- */
.sidebar-section{margin-bottom:20px}
.sidebar-section-title{
  font-size:10px;font-weight:600;text-transform:uppercase;
  letter-spacing:.6px;color:var(--text-tertiary);
  margin-bottom:8px;
}
.sidebar-tag-cloud{display:flex;flex-wrap:wrap;gap:5px}
.sidebar-link{
  display:block;padding:3px 0;
  font-size:12px;color:var(--text-secondary);
  transition:color .12s;
}
.sidebar-link:hover{color:var(--text-heading)}

/* --- Footer --- */
.footer{
  padding:12px 24px;
  font-size:12px;color:var(--text-tertiary);
  border-top:1px solid var(--border);
  background:var(--surface);
}

/* --- Article Detail --- */
.article-detail{
  max-width:800px;margin:0 auto;
  padding:32px 40px;
}
.back-link{
  display:inline-flex;align-items:center;gap:4px;
  font-size:13px;color:var(--text-secondary);margin-bottom:20px;
}
.back-link:hover{color:var(--accent)}
.article-detail-header{margin-bottom:24px;padding-bottom:16px;border-bottom:1px solid var(--border)}
.article-detail-title{font-size:24px;font-weight:600;line-height:1.35;color:var(--text-heading)}
.article-detail-meta{font-size:13px;color:var(--text-tertiary);margin-top:8px}
.article-body h1,.article-body h2,.article-body h3{margin-top:1.8em;margin-bottom:.4em;line-height:1.35;color:var(--text-heading)}
.article-body h1{font-size:22px;font-weight:600}
.article-body h2{font-size:18px;font-weight:600}
.article-body h3{font-size:16px;font-weight:600}
.article-body p,.article-body li{color:var(--text-primary);line-height:1.8;margin-bottom:.3em}
.article-body p+p{margin-top:.6em}
.article-body ul,.article-body ol{padding-left:1.4em;margin:.4em 0}
.article-body hr{border:none;border-top:1px solid var(--border);margin:24px 0}
@media(max-width:860px){.article-detail{padding:24px 20px}}
.article-body pre{
  overflow:auto;border-radius:6px;padding:14px;
  background:var(--surface);border:1px solid var(--border);
  font-size:13px;
}
.article-body code{background:#2a2a3e;padding:.15em .35em;border-radius:3px;font-size:13px}
.article-body pre code{background:transparent;padding:0}
.article-body a{color:var(--accent)}
.article-body a:hover{color:var(--accent-hover);text-decoration:underline}

/* --- Tables --- */
.article-body table{
  width:100%;max-width:100%;border-collapse:collapse;
  margin:16px 0 24px;font-size:13px;line-height:1.6;
  display:block;overflow-x:auto;-webkit-overflow-scrolling:touch;
}
.article-body th,.article-body td{
  padding:8px 12px;border-bottom:1px solid var(--border);
  text-align:left;vertical-align:top;
}
.article-body th{
  color:var(--text-secondary);font-weight:600;font-size:11px;
  text-transform:uppercase;letter-spacing:.3px;
}
.article-body tr:hover td{background:var(--surface-hover)}
.tbl-ranking td:nth-child(1){width:40px;text-align:center;white-space:nowrap}
.tbl-ranking td:nth-child(2){min-width:140px}
.tbl-ranking td:nth-child(3){white-space:nowrap}
.tbl-ranking td:nth-child(4){text-align:right;white-space:nowrap}
.tbl-ranking td:nth-child(5){min-width:160px}
.tbl-pricing td:nth-child(1){min-width:120px}
.tbl-pricing td:nth-child(2){white-space:nowrap}
.tbl-pricing td:nth-child(3){text-align:right;white-space:nowrap}
.tbl-pricing td:nth-child(4){text-align:right;white-space:nowrap}
.tbl-pricing td:nth-child(5){text-align:center;white-space:nowrap}
.tbl-category td:nth-child(1){min-width:120px}
.tbl-category td:nth-child(2){white-space:nowrap}
.tbl-category td:nth-child(3){text-align:center;white-space:nowrap}
.tbl-category td:nth-child(4){min-width:180px}

/* --- Search --- */
#search-results .list-row{display:none}
#search-results .list-row.match{display:flex}
#no-results{display:none;color:var(--text-secondary);padding:20px 24px}
.search-input-full{
  width:100%;background:var(--surface);
  border:1px solid var(--border);border-radius:6px;
  color:var(--text-primary);padding:10px 14px;font-size:14px;outline:none;
  margin-bottom:0;
}
.search-input-full:focus{border-color:var(--accent)}

/* --- Health Banner --- */
.health-banner{
  background:rgba(255,180,50,.08);border-bottom:1px solid rgba(255,180,50,.15);
  padding:8px 24px;font-size:13px;color:var(--text-secondary);
}
.health-banner strong{color:rgba(255,180,50,.9)}

/* --- Category Cards (for Claude pages) --- */
.cat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1px;background:var(--border)}
.cat-card{
  padding:12px 16px;background:var(--bg);
  transition:background .12s;
}
.cat-card:hover{background:var(--surface-hover)}
.cat-card-name{font-size:14px;font-weight:500;color:var(--text-heading)}
.cat-card-desc{font-size:12px;color:var(--text-secondary);margin-top:2px}
.cat-card-link{font-size:12px;color:var(--accent);margin-top:4px;display:inline-block}

/* --- Empty State --- */
.empty-state{padding:40px 24px;text-align:center;color:var(--text-tertiary);font-size:14px}

/* --- Favorites --- */
.fav-tag{
  display:inline-block;
  background:#2a2a3e;
  color:var(--accent);
  padding:1px 8px;border-radius:10px;
  font-size:11px;line-height:1.6;
  text-decoration:none;
  transition:background .12s;
}
.fav-tag:hover{background:#353550}
.fav-tag+.fav-tag{margin-left:4px}
.fav-memo{font-size:12px;color:var(--text-tertiary);margin-top:2px;font-style:italic}
.fav-source{
  display:inline-block;font-size:11px;
  color:var(--text-tertiary);margin-left:8px;
}

/* --- Article Day Navigation --- */
.day-nav{
  display:flex;justify-content:space-between;align-items:center;
  padding:16px 0;margin-top:24px;
  border-top:1px solid var(--border);
}
.day-nav a{
  display:inline-flex;align-items:center;gap:4px;
  font-size:13px;color:var(--text-secondary);
  padding:6px 12px;border-radius:4px;
  transition:background .12s,color .12s;
}
.day-nav a:hover{background:var(--surface-hover);color:var(--accent-hover)}
.day-nav .nav-placeholder{width:120px}

/* --- Utility --- */
.visually-hidden{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}
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
      const a = document.createElement('a');
      a.className = 'list-row';
      a.href = ROOT_PATH + '/' + item.url;
      a.innerHTML =
        '<div class="list-row-body">' +
        '<div class="list-row-title">' + escHtml(item.title) + '</div>' +
        '<div class="list-row-summary">' + escHtml((item.summary||'').slice(0,120)) + '</div>' +
        '</div>' +
        '<div class="list-row-meta"><span class="meta-date">' + escHtml(item.date) + '</span></div>';
      container.appendChild(a);
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
    root_rel = root_rel.rstrip("/")
    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{root_rel}/style.css">
</head>
<body class="app">
  <header class="topbar">
    <button class="mobile-menu-btn" id="menu-toggle" aria-label="Menu">☰</button>
    <div class="topbar-brand"><a href="{root_rel}/index.html">{SITE_TITLE}</a></div>
    <nav class="topbar-nav">
      <a href="{root_rel}/index.html">AI News</a>
      <a href="{root_rel}/claude/index.html">Claude</a>
      <a href="{root_rel}/models/index.html">Models</a>
      <a href="{root_rel}/tags/index.html">Tags</a>
      <a href="{root_rel}/favorites/index.html">Favorites</a>
      <a href="{root_rel}/search/index.html">Search</a>
    </nav>
    <div class="topbar-search">
      <input id="header-search" type="search" placeholder="Search…" autocomplete="off">
    </div>
  </header>
  {body_html}
  <script>const ROOT_PATH="{root_rel}";</script>
  <script>{SEARCH_JS}</script>
  <script>
(function(){{
  var btn=document.getElementById('menu-toggle');
  if(!btn)return;
  btn.addEventListener('click',function(){{
    var sb=document.querySelector('.sidebar-left');
    if(sb)sb.classList.toggle('open');
  }});
  document.addEventListener('click',function(e){{
    var sb=document.querySelector('.sidebar-left');
    if(!sb||!sb.classList.contains('open'))return;
    if(!sb.contains(e.target)&&e.target!==btn)sb.classList.remove('open');
  }});
}})();
</script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# インデックスページ（ページネーション対応）
# ---------------------------------------------------------------------------

def _item_html(file: Path, root_rel: str) -> str:
    root_rel = root_rel.rstrip("/")
    rel_parts = file.relative_to(NEWS_DIR).parts
    year, month, filename = rel_parts
    day = filename.replace(".md", "")
    target = f"{root_rel}/news/{year}/{month}/{day}/index.html"

    raw = file.read_text(encoding="utf-8")
    meta, body = strip_front_matter(raw)
    title = article_title_from_body(body, day)
    bullets = extract_summary_bullets(body, max_lines=2)
    preview = " / ".join(html.escape(x) for x in bullets) if bullets else ""
    total_items = meta.get("total_items", "")

    tags = _parse_tags_from_meta(meta)
    tags_html = "".join(
        f'<span class="tag">{html.escape(t)}</span>'
        for t in tags[:4]
    )
    tags_row = f'<span class="tag-row">{tags_html}</span>' if tags_html else ""

    return f"""<a class="list-row" href="{target}">
      <div class="list-row-title">{html.escape(title)}</div>
      <div class="list-row-summary">{preview}</div>
      <div class="list-row-meta">
        <span class="meta-date">{html.escape(day)}</span>
        <span class="meta-count">{html.escape(str(total_items))}</span>
        {tags_row}
      </div>
    </a>"""


def _pagination_html(current_page: int, total_pages: int, root_rel: str) -> str:
    root_rel = root_rel.rstrip("/")
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

    detail_html = " / ".join(html.escape(d) for d in details)

    return f"""<div class="health-banner">
      <strong>収集健全性: 注意（{len(warnings)}件）</strong> — {detail_html}
    </div>"""


def _build_date_tree(files: list[Path], root_rel: str, current_ym: str = "") -> str:
    """年/月/日の折りたたみツリーHTMLを生成する。
    current_ym は 'YYYY/MM' 形式で、該当する年・月をデフォルトopenにする。
    """
    root_rel = root_rel.rstrip("/")
    from collections import OrderedDict
    # ファイルを year -> month -> [day, ...] に分類
    tree: dict[str, dict[str, list[tuple[str, str]]]] = OrderedDict()
    for file in files:
        rel_parts = file.relative_to(NEWS_DIR).parts
        year, month, filename = rel_parts
        day = filename.replace(".md", "")
        target = f"{root_rel}/news/{year}/{month}/{day}/index.html"
        tree.setdefault(year, OrderedDict()).setdefault(month, []).append((day, target))

    if not tree:
        return '<div class="side-section"><div class="side-heading">Daily Reports</div></div>'

    # 現在の年月を特定（current_ym がなければ最新ファイルから）
    if not current_ym and files:
        parts = files[0].relative_to(NEWS_DIR).parts
        current_ym = f"{parts[0]}/{parts[1]}"
    cur_year, cur_month = (current_ym.split("/", 1) + [""])[:2]

    parts_html = []
    for year, months in tree.items():
        year_open = " open" if year == cur_year else ""
        month_parts = []
        year_count = sum(len(days) for days in months.values())
        for month, days in months.items():
            month_open = " open" if year == cur_year and month == cur_month else ""
            day_links = "".join(
                f'<a class="side-link" href="{href}">{html.escape(day)}</a>'
                for day, href in days
            )
            month_parts.append(
                f'<details class="tree-month"{month_open}>'
                f'<summary>{html.escape(month)} <span class="side-count">{len(days)}</span></summary>'
                f'{day_links}</details>'
            )
        parts_html.append(
            f'<details class="tree-year"{year_open}>'
            f'<summary>{html.escape(year)} <span class="side-count">{year_count}</span></summary>'
            f'{"".join(month_parts)}</details>'
        )

    return f'<div class="side-tree"><div class="side-heading">Daily Reports</div>{"".join(parts_html)}</div>'


def _build_month_tabs(files: list[Path], active_month: str, root_rel: str) -> str:
    """月タブHTMLを生成する。active_month は 'YYYY-MM' or 'all'。"""
    root_rel = root_rel.rstrip("/")
    months: list[str] = []
    seen = set()
    for file in files:
        rel_parts = file.relative_to(NEWS_DIR).parts
        ym = f"{rel_parts[0]}-{rel_parts[1]}"
        if ym not in seen:
            seen.add(ym)
            months.append(ym)

    if not months:
        return ""

    tabs = []
    all_active = ' class="month-tab active"' if active_month == "all" else ' class="month-tab"'
    tabs.append(f'<a href="{root_rel}/index.html"{all_active}>All</a>')
    for ym in months:
        active = ' class="month-tab active"' if ym == active_month else ' class="month-tab"'
        tabs.append(f'<a href="{root_rel}/month/{ym}/index.html"{active}>{ym}</a>')

    return f'<div class="month-tabs">{"".join(tabs)}</div>'


def _collect_months(files: list[Path]) -> list[str]:
    """ファイル群からユニークな 'YYYY-MM' リスト (降順) を返す。"""
    seen = []
    s = set()
    for f in files:
        p = f.relative_to(NEWS_DIR).parts
        ym = f"{p[0]}-{p[1]}"
        if ym not in s:
            s.add(ym)
            seen.append(ym)
    return seen


def build_index_pages(files: list[Path], prev_files: list[Path] | None = None, test_files: list[Path] | None = None) -> None:
    total_pages = max(1, (len(files) + PAGE_SIZE - 1) // PAGE_SIZE)

    # 左サイドバー: 年/月ツリー
    date_tree_html = _build_date_tree(files, ".")

    # テスト記事リンク
    test_nav_links = ""
    if test_files:
        links = []
        for file in test_files[:10]:
            rel_parts = file.relative_to(NEWS_DIR).parts
            year, month, filename = rel_parts
            day = filename.replace(".md", "")
            target = f"news/{year}/{month}/{day}/index.html"
            label = day.replace("test-", "")
            links.append(f'<a class="side-link" href="{target}">{html.escape(label)}</a>')
        test_nav_links = f"""
        <div class="side-section">
          <div class="side-heading">Test</div>
          {"".join(links)}
        </div>"""

    # 保存記事リンク
    prev_nav_links = ""
    if prev_files:
        links = []
        for file in prev_files[:10]:
            rel_parts = file.relative_to(NEWS_DIR).parts
            year, month, filename = rel_parts
            day = filename.replace(".md", "")
            target = f"news/{year}/{month}/{day}/index.html"
            label = day.replace("prev-", "")
            links.append(f'<a class="side-link" href="{target}">{html.escape(label)}</a>')
        prev_nav_links = f"""
        <div class="side-section">
          <div class="side-heading">Saved</div>
          {"".join(links)}
        </div>"""

    # 右サイドバー: 全タグ集計
    all_tags: dict[str, int] = {}
    for file in files:
        raw = file.read_text(encoding="utf-8")
        meta, _ = strip_front_matter(raw)
        for t in _parse_tags_from_meta(meta):
            all_tags[t] = all_tags.get(t, 0) + 1
    tag_cloud_html = "".join(
        f'<a href="tags/{html.escape(_sanitize_dirname(t))}/index.html" class="tag">{html.escape(t)} {c}</a>'
        for t, c in sorted(all_tags.items(), key=lambda x: -x[1])
    )

    # 月タブ
    month_tabs = _build_month_tabs(files, "all", ".")

    for page_num in range(1, total_pages + 1):
        start = (page_num - 1) * PAGE_SIZE
        page_files = files[start: start + PAGE_SIZE]

        items_html = [_item_html(f, ".") for f in page_files]

        pagination = _pagination_html(page_num, total_pages, ".")

        health_banner = _build_health_banner() if page_num == 1 else ""

        body_html = f"""
  {health_banner}
  <div class="layout">
    <aside class="sidebar-left">
      {date_tree_html}
      {test_nav_links}
      {prev_nav_links}
    </aside>
    <main class="content-area">
      <div class="content-header">
        <div class="content-title">{"All AI News" if page_num == 1 else f"Page {page_num}"}</div>
        <div class="content-subtitle">{len(files)} daily reports</div>
        {month_tabs}
      </div>
      <div class="list-view">
        {''.join(items_html) if items_html else '<div class="empty-state">No reports yet.</div>'}
      </div>
      {pagination}
    </main>
    <aside class="sidebar-right">
      <div class="sidebar-section">
        <div class="sidebar-section-title">Tags</div>
        <div class="sidebar-tag-cloud">
          {tag_cloud_html if tag_cloud_html else '<span style="color:var(--text-tertiary);font-size:12px">No tags</span>'}
        </div>
      </div>
      <div class="sidebar-section">
        <div class="sidebar-section-title">Links</div>
        <a class="sidebar-link" href="claude/index.html">Claude Info</a>
        <a class="sidebar-link" href="models/index.html">Model Report</a>
        <a class="sidebar-link" href="favorites/index.html">Favorites</a>
        <a class="sidebar-link" href="search/index.html">Search</a>
      </div>
    </aside>
  </div>
  <footer class="footer">Built automatically from daily Markdown files.</footer>"""

        page_title = SITE_TITLE if page_num == 1 else f"{SITE_TITLE} - Page {page_num}"
        html_text = page_shell(page_title, body_html, root_rel=".")

        if page_num == 1:
            (SITE_DIR / "index.html").write_text(html_text, encoding="utf-8")
        else:
            page_dir = SITE_DIR / "page" / str(page_num)
            page_dir.mkdir(parents=True, exist_ok=True)
            (page_dir / "index.html").write_text(html_text, encoding="utf-8")

    # --- 月別ページ生成 ---
    months = _collect_months(files)
    for ym in months:
        y, m = ym.split("-")
        month_files = [f for f in files if f.relative_to(NEWS_DIR).parts[0] == y and f.relative_to(NEWS_DIR).parts[1] == m]
        if not month_files:
            continue

        items_html = [_item_html(f, "../..") for f in month_files]
        month_tabs_html = _build_month_tabs(files, ym, "../..")
        tree_html = _build_date_tree(files, "../..", current_ym=f"{y}/{m}")

        month_body = f"""
  <div class="layout">
    <aside class="sidebar-left">
      {tree_html}
    </aside>
    <main class="content-area">
      <div class="content-header">
        <div class="content-title">{html.escape(ym)}</div>
        <div class="content-subtitle">{len(month_files)} reports</div>
        {month_tabs_html}
      </div>
      <div class="list-view">
        {''.join(items_html)}
      </div>
    </main>
    <aside class="sidebar-right">
      <div class="sidebar-section">
        <div class="sidebar-section-title">Tags</div>
        <div class="sidebar-tag-cloud">
          {tag_cloud_html if tag_cloud_html else '<span style="color:var(--text-tertiary);font-size:12px">No tags</span>'}
        </div>
      </div>
    </aside>
  </div>"""

        month_dir = SITE_DIR / "month" / ym
        month_dir.mkdir(parents=True, exist_ok=True)
        (month_dir / "index.html").write_text(
            page_shell(f"{ym} - {SITE_TITLE}", month_body, root_rel="../.."),
            encoding="utf-8",
        )

    if months:
        print(f"[info] built {len(months)} month page(s): {', '.join(months)}")


# ---------------------------------------------------------------------------
# 記事詳細ページ
# ---------------------------------------------------------------------------

def _day_nav_html(files: list[Path], idx: int) -> str:
    """前日・翌日ナビゲーションHTMLを返す。files は降順（新しい順）。"""
    # files は降順なので idx-1 が翌日、idx+1 が前日
    prev_link = ""
    next_link = ""

    if idx + 1 < len(files):
        p = files[idx + 1].relative_to(NEWS_DIR).parts
        py, pm, pf = p
        pd = pf.replace(".md", "")
        prev_link = f'<a href="../../../../news/{py}/{pm}/{pd}/index.html">← {pd}</a>'

    if idx - 1 >= 0:
        n = files[idx - 1].relative_to(NEWS_DIR).parts
        ny, nm, nf = n
        nd = nf.replace(".md", "")
        next_link = f'<a href="../../../../news/{ny}/{nm}/{nd}/index.html">{nd} →</a>'

    if not prev_link and not next_link:
        return ""

    return f"""<div class="day-nav">
          {prev_link if prev_link else '<span class="nav-placeholder"></span>'}
          {next_link if next_link else '<span class="nav-placeholder"></span>'}
        </div>"""


def build_article_pages(files: list[Path]) -> None:
    for idx, file in enumerate(files):
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
            f'<a href="../../../../tags/{html.escape(_sanitize_dirname(t))}/index.html" class="tag">{html.escape(t)}</a>'
            for t in tags
        )
        tags_row = f'<div class="tag-row" style="margin-top:8px">{tags_html}</div>' if tags_html else ""

        day_nav = _day_nav_html(files, idx)

        body_html = f"""
  <div class="layout">
    <main class="content-area">
      <div class="article-detail">
        <a class="back-link" href="../../../../index.html">← Back to list</a>
        <div class="article-detail-header">
          <h1 class="article-detail-title">{html.escape(title)}</h1>
          <div class="article-detail-meta">
            {html.escape(meta.get('date', day))} / {html.escape(meta.get('total_items', ''))} items
          </div>
          {tags_row}
        </div>
        <div class="article-body">
          {article_html}
        </div>
        {day_nav}
      </div>
    </main>
  </div>"""

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

    # 左サイドバーにタグナビ
    side_tag_links = "".join(
        f'<a class="side-link" href="{html.escape(_sanitize_dirname(tag))}/index.html">'
        f'{html.escape(tag)}<span class="side-count">{len(flist)}</span></a>'
        for tag, flist in sorted(tag_to_files.items(), key=lambda x: -len(x[1]))
    )

    tag_cloud = "".join(
        f'<a href="{html.escape(_sanitize_dirname(tag))}/index.html" class="tag">'
        f'{html.escape(tag)} ({len(flist)})</a>'
        for tag, flist in sorted(tag_to_files.items(), key=lambda x: -len(x[1]))
    )
    overview_body = f"""
  <div class="layout">
    <aside class="sidebar-left">
      <div class="side-section">
        <div class="side-heading">All Tags</div>
        {side_tag_links}
      </div>
    </aside>
    <main class="content-area">
      <div class="content-header">
        <div class="content-title">Tags</div>
        <div class="content-subtitle">{len(tag_to_files)} tags</div>
      </div>
      <div style="padding:16px 24px">
        <div class="sidebar-tag-cloud" style="gap:6px">
          {tag_cloud if tag_cloud else '<div class="empty-state">No tags.</div>'}
        </div>
      </div>
    </main>
  </div>"""
    (tags_dir / "index.html").write_text(
        page_shell("Tags - " + SITE_TITLE, overview_body, root_rel=".."),
        encoding="utf-8",
    )

    # 各タグの記事一覧ページ
    for tag, tag_files in tag_to_files.items():
        items_html = [_item_html(f, "../..") for f in tag_files]

        body_html = f"""
  <div class="layout">
    <aside class="sidebar-left">
      <div class="side-section">
        <div class="side-heading">All Tags</div>
        {side_tag_links}
      </div>
    </aside>
    <main class="content-area">
      <div class="content-header">
        <div class="content-title">{html.escape(tag)}</div>
        <div class="content-subtitle">{len(tag_files)} articles</div>
      </div>
      <div class="list-view">
        {''.join(items_html)}
      </div>
    </main>
  </div>"""

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
  <div class="layout">
    <main class="content-area">
      <div class="content-header" style="display:flex;align-items:center;gap:12px">
        <div class="content-title" style="flex-shrink:0">Search</div>
        <input id="search-input" class="search-input-full" type="search"
          placeholder="Type to search…" autocomplete="off" style="flex:1">
      </div>
      <div id="no-results">No matching articles found.</div>
      <div id="search-page-results" class="list-view"></div>
    </main>
  </div>"""

    (search_dir / "index.html").write_text(
        page_shell("Search - " + SITE_TITLE, body_html, root_rel=".."),
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

    body_html = f"""
  <div class="layout">
    <main class="content-area">
      <div class="article-detail">
        <a class="back-link" href="{back_href}">{back_label}</a>
        <div class="article-detail-header">
          <h1 class="article-detail-title">{html.escape(title)}</h1>
          <div class="article-detail-meta">Last updated: {html.escape(report_date)}</div>
        </div>
        <div class="article-body">
          {article_html}
        </div>
        {history_links_html}
      </div>
    </main>
  </div>"""

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
                f'class="tag">{html.escape(date_str)}</a>'
            )
        history_links = f"""
        <div style="margin-top:24px;padding-top:16px;border-top:1px solid var(--border)">
          <div style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--text-tertiary);margin-bottom:8px">History</div>
          <div class="sidebar-tag-cloud" style="gap:6px">
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
    root_rel = root_rel.rstrip("/")
    target = f"{root_rel}/claude/{category}/{slug}/index.html"
    date_str = meta.get("date", "")
    tags = _parse_tags_from_meta(meta)
    tags_html = "".join(
        f'<span class="tag">{html.escape(t)}</span>'
        for t in tags[:5]
    )
    tags_row = f'<div class="tag-row">{tags_html}</div>' if tags_html else ''

    return f"""<a class="list-row" href="{target}">
      <div class="list-row-title">{html.escape(title)}</div>
      <div class="list-row-summary">{html.escape(summary)}</div>
      <div class="list-row-meta">
        <span class="meta-date">{html.escape(date_str)}</span>
        <span class="tag">{html.escape(category)}</span>
        {tags_row}
      </div>
    </a>"""


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
        count_text = f'{cnt} articles' if cnt > 0 else 'Coming soon'
        link = f'<a class="cat-card-link" href="category/{cat_dir}/index.html">View →</a>' if cnt > 0 else ''
        cat_cards_html.append(f"""
          <div class="cat-card">
            <div class="cat-card-name">{html.escape(cat_label)} <span style="color:var(--text-tertiary);font-size:12px">({count_text})</span></div>
            <div class="cat-card-desc">{html.escape(cat_desc)}</div>
            {link}
          </div>""")

    # --- サイドナビ HTML（記事があるカテゴリのみリンク） ---
    side_links = []
    for cat_dir, cat_label, _ in _CLAUDE_CATEGORIES:
        cnt = cat_counts.get(cat_dir, 0)
        if cnt > 0:
            side_links.append(
                f'<a class="side-link" href="category/{cat_dir}/index.html">'
                f'{html.escape(cat_label)}<span class="side-count">{cnt}</span></a>'
            )
        else:
            side_links.append(
                f'<span class="side-link" style="color:rgba(255,255,255,.2);cursor:default">'
                f'{html.escape(cat_label)}<span class="side-count">0</span></span>'
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
  <div class="layout">
    <aside class="sidebar-left">
      <div class="side-section">
        <div class="side-heading">Categories</div>
        {side_nav_html}
      </div>
    </aside>
    <main class="content-area">
      <div class="content-header">
        <div class="content-title">Claude Ecosystem</div>
        <div class="content-subtitle">{len(articles)} articles</div>
      </div>
      <div class="cat-grid">
        {''.join(cat_cards_html)}
      </div>
      <div class="list-view">
        {articles_section}
      </div>
    </main>
    <aside class="sidebar-right">
      <div class="sidebar-section">
        <div class="sidebar-section-title">Navigation</div>
        <a class="sidebar-link" href="../index.html">Daily Reports</a>
        <a class="sidebar-link" href="../models/index.html">Model Report</a>
        <a class="sidebar-link" href="../search/index.html">Search</a>
      </div>
    </aside>
  </div>"""
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
  <div class="layout">
    <aside class="sidebar-left">
      <div class="side-section">
        <div class="side-heading">Categories</div>
        {side_nav_html.replace('category/', '../')}
      </div>
    </aside>
    <main class="content-area">
      <div class="content-header">
        <a class="back-link" href="../../index.html" style="margin-bottom:4px">← Claude Info</a>
        <div class="content-title">{html.escape(cat_label)}</div>
        <div class="content-subtitle">{len(cat_articles)} articles</div>
      </div>
      <div class="list-view">
        {''.join(items_html)}
      </div>
    </main>
  </div>"""

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
            f'<span class="tag">{html.escape(t)}</span>'
            for t in tags
        )
        tags_row = f'<div class="tag-row" style="margin-top:8px">{tags_html}</div>' if tags_html else ""

        detail_body = f"""
  <div class="layout">
    <main class="content-area">
      <div class="article-detail">
        <a class="back-link" href="../../index.html">← Claude Info</a>
        <div class="article-detail-header">
          <h1 class="article-detail-title">{html.escape(title)}</h1>
          <div class="article-detail-meta">{html.escape(cat_label)} / Updated: {html.escape(updated)}</div>
          {tags_row}
        </div>
        <div class="article-body">
          {article_html}
        </div>
      </div>
    </main>
  </div>"""

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
# お気に入りページ
# ---------------------------------------------------------------------------

FAV_FILE = BASE_DIR / "data" / "favorites.yaml"


def _load_favorites() -> list[dict]:
    if not FAV_FILE.exists():
        return []
    with open(FAV_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("favorites", []) or []


def _fav_item_html(fav: dict, root_rel: str) -> str:
    """お気に入り記事の一覧アイテムHTMLを返す。"""
    root_rel = root_rel.rstrip("/")
    title = fav.get("title", fav.get("url", ""))
    url = fav.get("url", "")
    source_date = fav.get("source_date", "")
    added = fav.get("added", "")
    memo = fav.get("memo", "")
    user_tags = fav.get("user_tags", [])

    tags_html = "".join(
        f'<a class="fav-tag" href="{root_rel}/favorites/tags/{html.escape(_sanitize_dirname(t))}/index.html">{html.escape(t)}</a>'
        for t in user_tags
    )
    memo_html = f'<div class="fav-memo">{html.escape(memo)}</div>' if memo else ""

    return f"""<a class="list-row" href="{html.escape(url)}" target="_blank" rel="noopener">
      <div class="list-row-title">{html.escape(title)}</div>
      {memo_html}
      <div class="list-row-meta">
        <span class="meta-date">{html.escape(source_date)}</span>
        <span class="fav-source">added {html.escape(added)}</span>
        <span class="tag-row">{tags_html}</span>
      </div>
    </a>"""


def build_favorites_pages() -> None:
    """お気に入りページを _site/favorites/ に生成する。"""
    favorites = _load_favorites()
    fav_dir = SITE_DIR / "favorites"
    fav_dir.mkdir(parents=True, exist_ok=True)

    # タグ集計
    tag_to_favs: dict[str, list[dict]] = {}
    for fav in favorites:
        for t in fav.get("user_tags", []):
            tag_to_favs.setdefault(t, []).append(fav)

    # サイドバー: タグナビ
    side_tag_links = ""
    if tag_to_favs:
        side_tag_links = "".join(
            f'<a class="side-link" href="tags/{html.escape(_sanitize_dirname(tag))}/index.html">'
            f'{html.escape(tag)}<span class="side-count">{len(flist)}</span></a>'
            for tag, flist in sorted(tag_to_favs.items(), key=lambda x: -len(x[1]))
        )

    # --- 全件一覧ページ ---
    items_html = [_fav_item_html(f, "..") for f in favorites]

    tag_cloud = ""
    if tag_to_favs:
        tag_cloud = "".join(
            f'<a href="tags/{html.escape(_sanitize_dirname(tag))}/index.html" class="fav-tag">'
            f'{html.escape(tag)} ({len(flist)})</a>'
            for tag, flist in sorted(tag_to_favs.items(), key=lambda x: -len(x[1]))
        )

    body_html = f"""
  <div class="layout">
    <aside class="sidebar-left">
      <div class="side-section">
        <div class="side-heading">Favorite Tags</div>
        {side_tag_links if side_tag_links else '<span class="side-link" style="color:rgba(255,255,255,.2)">No tags yet</span>'}
      </div>
    </aside>
    <main class="content-area">
      <div class="content-header">
        <div class="content-title">Favorites</div>
        <div class="content-subtitle">{len(favorites)} articles</div>
      </div>
      <div style="padding:12px 24px">
        <div class="sidebar-tag-cloud" style="gap:6px">
          {tag_cloud if tag_cloud else ""}
        </div>
      </div>
      <div class="list-view">
        {''.join(items_html) if items_html else '<div class="empty-state">No favorites yet. Use <code>python -m scripts.favorites add URL --tags tag1,tag2</code> to add.</div>'}
      </div>
    </main>
  </div>"""

    (fav_dir / "index.html").write_text(
        page_shell("Favorites - " + SITE_TITLE, body_html, root_rel=".."),
        encoding="utf-8",
    )

    # --- タグ別ページ ---
    tags_dir = fav_dir / "tags"
    for tag, tag_favs in tag_to_favs.items():
        items_html = [_fav_item_html(f, "../../..") for f in tag_favs]

        tag_body = f"""
  <div class="layout">
    <aside class="sidebar-left">
      <div class="side-section">
        <div class="side-heading">Favorite Tags</div>
        {side_tag_links.replace('tags/', '../')}
      </div>
    </aside>
    <main class="content-area">
      <div class="content-header">
        <a class="back-link" href="../../index.html">← Favorites</a>
        <div class="content-title">{html.escape(tag)}</div>
        <div class="content-subtitle">{len(tag_favs)} articles</div>
      </div>
      <div class="list-view">
        {''.join(items_html)}
      </div>
    </main>
  </div>"""

        tag_dir = tags_dir / _sanitize_dirname(tag)
        tag_dir.mkdir(parents=True, exist_ok=True)
        (tag_dir / "index.html").write_text(
            page_shell(f"{tag} - Favorites - {SITE_TITLE}", tag_body, root_rel="../../.."),
            encoding="utf-8",
        )

    print(f"[info] built favorites: {len(favorites)} article(s), {len(tag_to_favs)} tag(s)")


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
    build_favorites_pages()

    print(f"[info] built site: {SITE_DIR}")
    print(f"[info]   {len(files)} articles, {len(prev_files)} prev articles, {max(1, (len(files) + PAGE_SIZE - 1) // PAGE_SIZE)} index page(s)")


if __name__ == "__main__":
    main()
