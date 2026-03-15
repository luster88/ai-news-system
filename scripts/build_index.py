from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
NEWS_DIR = BASE_DIR / "news"
INDEX_FILE = BASE_DIR / "index.md"


def build_index():
    files = sorted(
        NEWS_DIR.glob("*/*/*.md"),
        reverse=True,
    )

    lines = []
    lines.append("# AI News Daily Index")
    lines.append("")
    lines.append("最新のAIニュース日報一覧です。")
    lines.append("")

    if not files:
        lines.append("- まだ日報がありません。")
    else:
        lines.append("## 最新日報")
        lines.append("")

        for file in files[:30]:
            rel = file.relative_to(BASE_DIR).as_posix()
            date_label = file.stem
            lines.append(f"- [{date_label}]({rel})")

    INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")
    return str(INDEX_FILE)