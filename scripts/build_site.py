from pathlib import Path
from datetime import datetime
import html
import re

import markdown

BASE_DIR = Path(__file__).resolve().parent.parent
NEWS_DIR = BASE_DIR / "news"
SITE_DIR = BASE_DIR / "_site"

SITE_TITLE = "AI News Daily"


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
  gap:16px; padding:14px 0;
}
.brand{
  font-weight:800; letter-spacing:.2px; font-size:20px;
}
.brand a{color:var(--text); text-decoration:none}
.sub{
  color:var(--muted); font-size:14px;
}
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
.back{
  margin-bottom:16px;
  display:inline-block;
}
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
    return sorted(NEWS_DIR.glob("*/*/*.md"), reverse=True)


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
      <div class="sub">GitHub Pages static site</div>
    </div>
  </header>
  {body_html}
  <footer class="footer">
    <div class="wrap">Built automatically from daily Markdown files.</div>
  </footer>
</body>
</html>
"""


def build_index(files: list[Path]) -> None:
    items_html = []

    for file in files[:30]:
        rel_parts = file.relative_to(NEWS_DIR).parts
        year, month, filename = rel_parts
        day = filename.replace(".md", "")
        target = f"news/{year}/{month}/{day}/index.html"

        raw = file.read_text(encoding="utf-8")
        meta, body = strip_front_matter(raw)
        title = article_title_from_body(body, day)
        bullets = extract_summary_bullets(body, max_lines=2)
        preview = " / ".join(html.escape(x) for x in bullets) if bullets else "日報を開く"

        total_items = meta.get("total_items", "")
        items_html.append(f"""
        <article class="item">
          <h3><a href="{target}">{html.escape(title)}</a></h3>
          <div class="meta">
            <span class="chip">{html.escape(day)}</span>
            <span class="chip">{html.escape(total_items)} items</span>
          </div>
          <p class="preview">{preview}</p>
        </article>
        """)

    latest_links = []
    for file in files[:14]:
        rel_parts = file.relative_to(NEWS_DIR).parts
        year, month, filename = rel_parts
        day = filename.replace(".md", "")
        target = f"news/{year}/{month}/{day}/index.html"
        latest_links.append(f'<a href="{target}">{html.escape(day)}</a>')

    body_html = f"""
    <main class="wrap">
      <section class="hero">
        <div class="hero-card">
          <h1>{SITE_TITLE}</h1>
          <p>毎日の AI ツール / 企業動向 / 業界ニュースを Markdown から自動で静的サイト化しています。</p>
        </div>
      </section>

      <section class="grid">
        <div class="card">
          <h2>最新日報</h2>
          <div class="list">
            {''.join(items_html) if items_html else '<p class="preview">まだ日報がありません。</p>'}
          </div>
        </div>

        <aside class="card">
          <h2>最近の日付</h2>
          <div class="side-list">
            {''.join(latest_links) if latest_links else '<div class="preview">まだ日報がありません。</div>'}
          </div>
        </aside>
      </section>
    </main>
    """

    html_text = page_shell(SITE_TITLE, body_html, root_rel=".")
    (SITE_DIR / "index.html").write_text(html_text, encoding="utf-8")


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

        body_html = f"""
        <main class="wrap article">
          <a class="back" href="../../../../index.html">← index に戻る</a>
          <article class="article-card">
            <div class="article-header">
              <h1 class="article-title">{html.escape(title)}</h1>
              <div class="article-meta">
                date: {html.escape(meta.get('date', day))} / total_items: {html.escape(meta.get('total_items', ''))}
              </div>
            </div>
            <div class="article-body">
              {article_html}
            </div>
          </article>
        </main>
        """

        html_text = page_shell(title, body_html, root_rel="../../../../")
        (out_dir / "index.html").write_text(html_text, encoding="utf-8")


def main():
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "style.css").write_text(CSS, encoding="utf-8")
    (SITE_DIR / ".nojekyll").write_text("", encoding="utf-8")

    files = read_news_files()
    build_index(files)
    build_article_pages(files)

    print(f"[info] built site: {SITE_DIR}")


if __name__ == "__main__":
    main()