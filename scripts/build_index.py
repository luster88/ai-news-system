import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
NEWS_DIR = BASE_DIR / "news"
MODELS_DIR = BASE_DIR / "models"
INDEX_FILE = BASE_DIR / "index.md"


def _read_model_report_date() -> str:
    """models/latest.md のフロントマターから日付を読み取る。"""
    latest = MODELS_DIR / "latest.md"
    if not latest.exists():
        return ""
    text = latest.read_text(encoding="utf-8")
    m = re.search(r"^date:\s*(\S+)", text, re.MULTILINE)
    return m.group(1) if m else ""


def build_index():
    all_files = sorted(NEWS_DIR.glob("*/*/*.md"), reverse=True)
    files = [f for f in all_files if not f.name.startswith("prev-") and not f.name.startswith("test-")]
    test_files = [f for f in all_files if f.name.startswith("test-")]
    prev_files = [f for f in all_files if f.name.startswith("prev-")]

    model_date = _read_model_report_date()

    lines = []
    lines.append("# AI News Daily Index")
    lines.append("")
    lines.append("最新のAIニュース日報一覧です。")
    lines.append("")

    if model_date:
        lines.append(f"**[最新AIモデルまとめ（{model_date} 時点）](models/latest.md)**")
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

    if test_files:
        lines.append("")
        lines.append("## テスト記事")
        lines.append("")

        for file in test_files[:30]:
            rel = file.relative_to(BASE_DIR).as_posix()
            # test-sonnet-2026-03-22-0830 → sonnet 2026-03-22 08:30
            label = file.stem.replace("test-", "")
            lines.append(f"- [{label}]({rel})")

    if prev_files:
        lines.append("")
        lines.append("## 保存記事")
        lines.append("")

        for file in prev_files[:30]:
            rel = file.relative_to(BASE_DIR).as_posix()
            date_label = file.stem.replace("prev-", "")
            lines.append(f"- [{date_label} (保存)]({rel})")

    INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")
    return str(INDEX_FILE)