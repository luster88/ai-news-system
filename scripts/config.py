"""
config.py — プロジェクト設定の一元読み込み

data/config.yaml から設定値を読み込む。
ファイルが存在しない場合やキーが欠けている場合は、
各モジュール側のデフォルト値にフォールバックする。
"""

from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "data" / "config.yaml"

_config: dict = {}


def _load() -> dict:
    if not CONFIG_FILE.exists():
        return {}
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"[warn] config.yaml の読み込みに失敗しました: {e}")
        return {}


_config = _load()


def get(key: str, default=None):
    """設定値を取得する。キーがなければ default を返す。"""
    return _config.get(key, default)
