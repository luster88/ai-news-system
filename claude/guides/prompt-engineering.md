---
title: Prompt Engineering
category: guides
subcategory: prompt-engineering
tags:
- claude-api
- claude-code
- cowork
- haiku
- opus
- performance
- prompt
- setup
date: '2026-04-07'
updated: '2026-07-19'
sources:
- url: https://zenn.dev/analysis/articles/thought-analyzer-agents-md
  title: コンテキストファイルは、エージェントを賢くしない ── AGENTS.mdの効果を初めて測った研究
  date: '2026-04-07'
- url: https://qiita.com/ssk00226/items/0f039aa8a22e4f97f0b0
  title: 将棋エンジンの読み筋をLLMに解説させたら、ClaudeとChatGPTで差が出た話
  date: '2026-05-18'
- url: https://zenn.dev/uya0526_design/articles/satellite2_haiku-coaching
  title: Claude Haikuに「計算」をさせない ─ 音読コーチの二段構え設計とプロンプトの沼
  date: '2026-06-17'
- url: https://zenn.dev/takupeso/articles/claude-ontology-knowledge-structuring
  title: Claudeに「オントロジー」を持たせたら、コスト半分・3倍速になるかも
  date: '2026-06-27'
- url: https://zenn.dev/hayua/articles/5b6da584357698
  title: Fable 5 が消える前に、その「思考法」を Opus へ引き継げないか本気で試してみた
  date: '2026-07-07'
- url: https://zenn.dev/otoha_io/articles/1ed6059b794bfb
  title: 音声1本を「話し方を保ったまま」5つのSNS原稿にする — Claude二段生成の設計
  date: '2026-07-19'
---






# Prompt Engineering

---

## 2026-07-19

### 音声1本を「話し方を保ったまま」5つのSNS原稿にする — Claude二段生成の設計

個人開発ツールOTOHAで、1本の音声を話者の口調を保持したまま5つのSNS形式（X、Instagram、縦動画台本、note、メルマガ）に変換する設計を紹介。Claudeを使った二段階生成（前処理で口調プロファイルを抽出→各フォーマットに制約として適用）により、媒体間での人格のブレを防ぎ、並列処理で高速化を実現。幻覚を防ぐ共通ルールや語尾の自然さとの両立など、実装上の工夫と課題を詳しく解説。

- **ソース**: [Zenn claude](https://zenn.dev/otoha_io/articles/1ed6059b794bfb)
- **重要度**: 6/10
- **タグ**: prompt, haiku, cowork

---

## 2026-07-07

### Fable 5 が消える前に、その「思考法」を Opus へ引き継げないか本気で試してみた

Claude Fable 5のサブスク提供終了を前に、Fableの思考プロセスをskillとして書き出しOpusに引き継げるか検証した記事。Fableに自身の思考法を6つ抽出させ、汎用チェックリストと比較実験を実施。結果、Fable特有の上乗せ効果は確認できず、Opusは既に同等の思考能力を持っていたことが判明。AI評価バイアスを排除し、計算機で白黒つく問題のみで検証した点が特徴的。

- **ソース**: [Zenn claude](https://zenn.dev/hayua/articles/5b6da584357698)
- **重要度**: 6/10
- **タグ**: opus, prompt, performance

---

## 2026-06-27

### Claudeに「オントロジー」を持たせたら、コスト半分・3倍速になるかも

ClaudeCodeにナレッジを渡す際、従来の@指定やMarkdownの箇条書きはフラットな情報配置に過ぎず、概念間の関係性が欠如していることが、アウトプットのブレの原因となっていた。オントロジー（概念と関係を明示的に定義する手法）を導入することで、モデルに推測させず関係を確定させることができ、結果としてコスト半減・3倍速を実現できる可能性がある。従来のタグやフォルダと異なり、オントロジーはcalls、depends-onなど型付きの関係をグラフ構造で表現できる点が特徴。

- **ソース**: [Zenn claude](https://zenn.dev/takupeso/articles/claude-ontology-knowledge-structuring)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

---

## 2026-06-17

### Claude Haikuに「計算」をさせない ─ 音読コーチの二段構え設計とプロンプトの沼

音読速度計測アプリで、計算・判定ロジックをすべてコード側で確定させ、Claude Haikuには「整理済みの事実」を温かく具体的な言葉に翻訳させる「二段構え設計」を解説。役割分担により小さなモデルでも安定した出力を実現したが、プロンプトキャッシュは最小トークン数（4,096）に届かず実際には機能しなかったという検証結果も報告。LLMに計算させず言語化のみを担わせる実装のベストプラクティスとして有益。

- **ソース**: [Zenn claude](https://zenn.dev/uya0526_design/articles/satellite2_haiku-coaching)
- **重要度**: 6/10
- **タグ**: prompt, haiku, setup

---

## 2026-05-18

### 将棋エンジンの読み筋をLLMに解説させたら、ClaudeとChatGPTで差が出た話

将棋エンジン（水匠5）の解析結果を Claude と ChatGPT に解説させる比較実験。同じ局面・評価値・プロンプトで5種類の対象者向け解説を生成した結果、Claude は深い教材文と段階的説明に優れ、ChatGPT は簡潔で安定した表現が特徴的だった。LLM は単なる文章生成ではなく UX を左右する「解釈レイヤー」として機能することが示された。

- **ソース**: [Qiita claude](https://qiita.com/ssk00226/items/0f039aa8a22e4f97f0b0)
- **重要度**: 6/10
- **タグ**: prompt, claude-api, cowork

---

## 2026-04-07

### コンテキストファイルは、エージェントを賢くしない ── AGENTS.mdの効果を初めて測った研究

ETH Zurichの研究により、CLAUDE.mdやAGENTS.mdなどのコンテキストファイルがエージェントのタスク成功率を平均3%低下させ、コストを20%以上増加させることが判明。LLMが自動生成したコンテキストファイルは特に効果が低く、人間が書く場合も「LLMが推論できない固有情報」のみに絞るべきと結論。thought-analyzerのskill.md v3.0設計も同様の知見に基づき、不要な指示を削除して簡略化している。

- **ソース**: [Zenn claude](https://zenn.dev/analysis/articles/thought-analyzer-agents-md)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-07 | 自動生成 |
