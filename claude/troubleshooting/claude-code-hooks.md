---
title: Claude Code Hooks
category: troubleshooting
subcategory: claude-code-hooks
tags:
- bugfix
- claude-code
- cowork
- performance
- setup
date: '2026-06-03'
updated: '2026-11-16'
sources:
- url: https://zenn.dev/gudezou/articles/7e8235a27f0909
  title: Claude Code の終了フックから claude を呼び出すとなぜ暴走するのか
  date: '2026-06-03'
- url: https://qiita.com/yurukusa/items/5a4f67b7e0f732a3f7c4
  title: SubagentStop の hook が、サブエージェントを使っていないメインセッションでも発火する——マルチエージェントを hook で組む人の盲点
  date: '2026-06-25'
- url: https://qiita.com/miyoki_labs/items/5f44b709a49747520d50
  title: Claude CodeのStop hookが誤発火する原因と切り分け
  date: '2026-08-04'
- url: https://qiita.com/homhom44/items/594957a69690a39c7f82
  title: Claude Code でつまずいたときの切り分けメモ（2026-08-31）
  date: '2026-08-31'
- url: https://zenn.dev/sactechnologies/articles/d990489b0e759d
  title: Claude Code のフックは、静かに死ぬ — 117本を数えたら12本が呼ばれていなかった
  date: '2026-09-17'
- url: https://zenn.dev/starken/articles/claude-code-hook-gate-bash-bypass
  title: Claude Codeのフックで止めたはずの書き込みが、Bashのlnやtouchで通っていた
  date: '2026-10-23'
- url: https://qiita.com/homhom44/items/d1987dc6a459b10701ae
  title: Claude Code で "PreToolUse:Bash hook error" / "Stop hook error" が出たときの見分け方（終了コードの意味と、成功しても
    error と表示される件）
  date: '2026-11-15'
- url: https://zenn.dev/kagaribilab/articles/claude-code-stop-hook-loop
  title: goalを使わずStopフックを自作したら、Claude Codeが止まらず使用量が増え続けた
  date: '2026-11-16'
---








# Claude Code Hooks

---

## 2026-11-16

### goalを使わずStopフックを自作したら、Claude Codeが止まらず使用量が増え続けた

Claude Code で goal を使わず Stop フックを自作したところ、裏の仕事（テスト実行など）を待つ仕組みが不足していたため、7.5秒ごとに差し戻しループが発生。1回のセッションで16.5億トークンを消費し、Max 5x の週間枠が2割減少する事態に。公式の /goal は裏の仕事中は判定をスキップする仕組みがあるが、自作フックにはそれがなかった。最終的に差し戻しを1回に制限し、push フックで品質を担保する形に変更した。

- **ソース**: [Zenn claude](https://zenn.dev/kagaribilab/articles/claude-code-stop-hook-loop)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, performance

---

## 2026-11-15

### Claude Code で "PreToolUse:Bash hook error" / "Stop hook error" が出たときの見分け方（終了コードの意味と、成功しても error と表示される件）

Claude Code でフック実行時に表示される「hook error」は、終了コード2の意図的なブロックでも、それ以外の失敗でも同じように表示されるため、表示だけでは真の失敗か判断できない。フックスクリプトを単体で実行して終了コードを確認することで切り分けが可能。終了コード0が成功、2が意図的ブロック、それ以外が非ブロック失敗となる。表示上のバグとして GitHub issue #17088 で報告されている。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/d1987dc6a459b10701ae)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-10-23

### Claude Codeのフックで止めたはずの書き込みが、Bashのlnやtouchで通っていた

Claude Codeのフックで~/.claude配下への書き込みを制御しようとしたが、Bashコマンド（ln、touch、rsync等）がゲートを素通りし、逆に読み取り専用コマンド（ls、jq等）が誤検知で停止された。原因はmatcherがEdit|Writeのみで、Bashツール呼び出しではフックが起動しないこと、および正規表現の不完全さ。knowledge配下の書き込みも検査を回避する設計上の問題があった。

- **ソース**: [Zenn claude](https://zenn.dev/starken/articles/claude-code-hook-gate-bash-bypass)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-09-17

### Claude Code のフックは、静かに死ぬ — 117本を数えたら12本が呼ばれていなかった

Claude Code のフックが静かに失敗する6つのパターンを実例とともに報告。117本のフック中12本が実際には動いていなかった事例を基に、毎回ゼロから検証する監査スクリプト hook-doctor.py の設計思想を解説。エラーを出さずに死ぬフックの検出方法と予防策を提示。

- **ソース**: [Zenn claude](https://zenn.dev/sactechnologies/articles/d990489b0e759d)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-08-31

### Claude Code でつまずいたときの切り分けメモ（2026-08-31）

Claude Code 使用中に発生する /goal 実行時や stop hook での処理停止問題について、GitHub Issues で複数報告されている症状を実際に検証し、切り分け方法と対処法を整理した記事。手元での実行結果と公式 Issues の報告のみを根拠とした実践的なトラブルシューティングガイド。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/594957a69690a39c7f82)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

### Claude Code でつまずいたときの切り分けメモ（2026-08-31）

Claude Code 使用時に /goal コマンドや stop hook で処理が途中停止する問題について、GitHub Issues の報告を基に実際にコマンドを実行して確認した切り分けメモ。複数ユーザーが遭遇している症状の原因と対処方法を整理している。

- **ソース**: [Qiita claudecode](https://qiita.com/homhom44/items/594957a69690a39c7f82)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix

---

## 2026-08-04

### Claude CodeのStop hookが誤発火する原因と切り分け

Claude CodeのStop hookが誤発火する問題の詳細な切り分け記録。複数セッション並行時に、mtimeベースの変更検知が他セッションの書き込みを拾い、無限ループ的な警告を繰り返す現象が発生。ログ分析により、体感の「ブロック」と実際の記録「suggestion注入」が食い違うことも判明。共有フォルダ監視をmtimeのみで行う場合の根本的な問題を指摘。

- **ソース**: [Qiita claudecode](https://qiita.com/miyoki_labs/items/5f44b709a49747520d50)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-06-25

### SubagentStop の hook が、サブエージェントを使っていないメインセッションでも発火する——マルチエージェントを hook で組む人の盲点

Claude Code 2.1.186でSubagentStopフックがサブエージェント未使用のメインセッション終了時にも誤発火する回帰バグが報告された。これはマルチエージェント制御でフックを使う開発者にとって、削除・通知などの取り返しのつかない処理が意図せず実行されるリスクがある。対策として、stdinの内容を記録して実際の発火状況を観察し、SubagentStopフック内で文脈確認を行うことが推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/5a4f67b7e0f732a3f7c4)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, cowork

---

## 2026-06-03

### Claude Code の終了フックから claude を呼び出すとなぜ暴走するのか

Claude Code の SessionEnd フックから claude を起動すると無限ループが発生する問題を解説。終了フックは同期実行されるため重い処理で固まる危険性があり、再帰防止には環境変数による入口ガードが有効。実際の事故事例では数百回発火し利用上限に達した。

- **ソース**: [Zenn claude](https://zenn.dev/gudezou/articles/7e8235a27f0909)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-03 | 自動生成 |
