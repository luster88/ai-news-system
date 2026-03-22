---
title: "Claude Code セットアップガイド"
category: guides
subcategory: setup
tags: [claude-code, setup, windows, vscode, installation]
date: 2026-03-23
updated: 2026-03-23
sources:
  - url: "https://code.claude.com/docs/en/setup"
    title: "Claude Code Advanced Setup"
    date: 2026-03-23
  - url: "https://interworks.com/blog/2026/01/27/how-to-install-claude-code-on-windows-11/"
    title: "How to Install Claude Code on Windows 11"
    date: 2026-01-27
---

# Claude Code セットアップガイド

Claude Code のインストールから初期設定までの手順をまとめる。

---

## 前提条件

- **Node.js**: v18 以上
- **Git**: Git for Windows（Windows の場合）
- **ターミナル**: PowerShell / Git Bash / CMD いずれか
- **認証**: Claude Pro / Max / Team / Enterprise のいずれかのサブスクリプション、または Anthropic Console の API キー

---

## インストール

### Windows（PowerShell）

```powershell
irm https://claude.ai/install.ps1 | iex
```

### macOS / Linux

```bash
npm install -g @anthropic-ai/claude-code
```

### 確認

```bash
claude --version
```

---

## 初期設定

### 認証方式の選択

初回起動時に認証方式を選択する:

1. **Claude account with subscription**（推奨）— ブラウザ認証でログイン
2. **Anthropic Console API key** — API キーを直接入力

Claude のサブスクリプションがある場合は「1」を選択する。API キーは Anthropic Console (platform.claude.com) で発行可能。

### テキストスタイル

初回起動時にターミナルのテキストスタイルを選択する。後から `/config` で変更可能。

---

## Windows 固有の注意点

### PATH の設定

インストール後に `claude` コマンドが見つからない場合、PATH に `C:\Users\{ユーザー名}\.local\bin` が含まれているか確認する。

**手動で追加する方法:**
1. 「システムのプロパティ」→「環境変数」を開く
2. ユーザー環境変数の `PATH` を編集
3. `C:\Users\{ユーザー名}\.local\bin` を追加

管理者権限は不要。

### PowerShell の実行ポリシー

スクリプト実行がブロックされる場合:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Git Bash との併用

Git Bash から `claude` を起動する場合、`.bashrc` に PATH を追加する場合がある。

---

## VS Code 連携

### 拡張機能

Claude Code は VS Code との連携機能を備えている:

- プランプレビュー: Claude の作業計画を VS Code 上でリアルタイム確認
- 差分レビュー: 変更内容を VS Code のエディタで確認・承認
- ターミナル統合: VS Code の統合ターミナルで直接利用可能

---

## このプロジェクト（ai-news-system）での初期設定

1. リポジトリをクローン後、`.env` ファイルを作成:

```bash
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
```

2. Python 仮想環境をセットアップ:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

3. Claude Code セッション開始時に最初に読むべきファイル:
   - `docs/HANDOFF.md` — 引き継ぎドキュメント（現状把握）
   - `README.md` — プロジェクト概要

---

## 関連リンク

- [Claude Code アップデート履歴](../releases/claude-code-updates.md)
- [ツール比較](../tools/comparison.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-23 | 初版作成 |
