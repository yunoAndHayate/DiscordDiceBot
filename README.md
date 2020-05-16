# DiscordDiceBot

[![Python version](https://img.shields.io/badge/python-3.7-blue.svg)](https://python.org)

Discordで使うことができる、TRPG用のダイスボットです。
Python3.7.1で開発しています。


## クイックスタート
1. Git Cloneをします。

2. ターミナルで以下を実行し、Discord.py をインストールします。

```
$ py -3 -m pip install -U discord.py[voice]
```

3. [Discord Developer Portal](https://discord.com/developers/applications/)でBotのアカウントを作成し、あなたの持っているDiscordサーバに紐づけます。

3. config.example.json をコピーして config.json に改名し、中身にBotアカウントのトークンを入力します。

4. dicebot.bat を実行してください。


## Commands

discordのチャンネル上で使えるようになるコマンド群です。
ネタバレ防止機能で保護すると、シークレットダイスになります。


### 汎用ダイス

```
{ダイスの数}D{ダイスの種類}[修正値][目標値] {コメント}
```

任意のダイスを任意の個数振ることができます。
例えば `1d100 目星` と入力すると、100面ダイスを1個振ります。

修正値や目標値にも対応しています。
例えば `2d6+1>=5` と入力すると、6面ダイス2個の合計値+1の値で、目標値5に届くか判定します。


### 魔法学園RPGハーベスト用ダイス

```
magic {ダイスの個数}
```

[魔法学園RPGハーベスト](https://harvestrpg.com/)の仕様に基づいたダイスを振ることができます。

▼以下のような出力をします。

```
[ダイスロール] magic5 => 地水水風闇 (1, 2, 2, 4, 6)
```


## 参考文献

- [Pythonで実用Discord Bot(discordpy解説)](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)
- [魔法学園RPGハーベスト](https://harvestrpg.com/)