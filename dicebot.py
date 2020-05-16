# インストールした discord.py を読み込む
import discord
import re
import random
import math
import json

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 「1d100」とか発言したら、ダイスを振って返す
    command_match = re.match('(\|\|)?([1-9][0-9]*)[dDⅮｄ]([1-9][0-9]*)([\+\-\*\/][0-9]+)?([<>=]+[0-9]+)?\s*(.*)', message.content)
    if command_match:
        is_secret = command_match[1] == '||'
        dice_num = int(command_match[2])
        dice_size = int(command_match[3])
        constration_method = re.match('[^0-9]+', command_match[4])[0] if command_match[4] else None
        constration_num = int(re.search('[0-9]+', command_match[4])[0]) if command_match[4] else None
        comparison_method = re.match('[^0-9]+', command_match[5])[0] if command_match[5] else None
        comparison_num = int(re.search('[0-9]+', command_match[5])[0]) if command_match[5] else None
        comment = command_match[6].replace('||', '')

        # ダイスロール
        dicerolls = []
        for num in range(dice_num):
            dicerolls.append(random.randint(1, dice_size))

        # 結果の数値を計算
        result_num = sum(dicerolls)
        if constration_method == '+':
            result_num += constration_num
        elif constration_method == '-':
            result_num -= constration_num
        elif constration_method == '*':
            result_num *= constration_num
        elif constration_method == '/':
            result_num = math.floor(result_num/constration_num)
        else:
            constration_method = ''
            constration_num = ''

        # 比較をおこなう
        if comparison_method == '<':
            result_num = str(result_num) + (' 成功！' if result_num < comparison_num else ' 失敗……')
        elif comparison_method == '>':
            result_num = str(result_num) + (' 成功！' if result_num > comparison_num else ' 失敗……')
        elif comparison_method == '<=':
            result_num = str(result_num) + (' 成功！' if result_num <= comparison_num else ' 失敗……')
        elif comparison_method == '>=':
            result_num = str(result_num) + (' 成功！' if result_num >= comparison_num else ' 失敗……')
        else:
            comparison_method = ''
            comparison_num = ''

        # 結果を出力
        if is_secret:
            result_text = '[シークレットダイス] ||'
        else:
            result_text = '[ダイスロール]'
        
        result_text += ' ' + str(dice_num) + 'D' + str(dice_size)
        result_text += str(constration_method)
        result_text += str(constration_num)
        result_text += ' ' + comparison_method if len(comparison_method)>0 else ''
        result_text += str(comparison_num)

        result_text += ' => ' + str(result_num)
        
        
        if 1 < len(dicerolls):
            maped_list = map(str, dicerolls)
            result_text += ' (' + ', '.join(maped_list) + ')'

        if is_secret:
            result_text += '||'

        if len(comment):
            result_text += '\r\n'
            if is_secret:
                result_text += '||'
            result_text += comment
            if is_secret:
                result_text += '||'

        # 出力する
        print(result_text.replace('\r\n',' '))
        await message.channel.send(result_text)

    # ハーベストのダイス。「magic8」とか入力すると発生したマナを教えてくれる
    command_match = re.match('(\|\|)?[mM][aA][gG][iI][cC]\s?([1-9][0-9]*)\s*(.*)', message.content)
    if command_match:
        is_secret = command_match[1] == '||'
        dice_num = int(command_match[2])
        dice_size = 6
        comment = command_match[3].replace('||', '')

        # ダイスロール
        dicerolls = []
        for num in range(dice_num):
            dicerolls.append(random.randint(1, dice_size))

        # 結果を出力
        if is_secret:
            result_text = '[シークレットダイス] ||'
        else:
            result_text = '[ハーベスト]'
        
        result_text += ' magic' + str(dice_num)
        dicerolls.sort()
        result_text += ' => '

        manas = []
        for key in range(len(dicerolls)):
            if dicerolls[key]==1:
                manas.insert(key, '地')
            elif dicerolls[key]==2:
                manas.insert(key, '水')
            elif dicerolls[key]==3:
                manas.insert(key, '火')
            elif dicerolls[key]==4:
                manas.insert(key, '風')
            elif dicerolls[key]==5:
                manas.insert(key, '光')
            elif dicerolls[key]==6:
                manas.insert(key, '闇')
        result_text += ''.join(manas)
        maped_list = map(str, dicerolls)
        result_text += ' (' + ', '.join(maped_list) + ')'

        if is_secret:
            result_text += '||'

        if len(comment):
            result_text += '\r\n'
            if is_secret:
                result_text += '||'
            result_text += comment
            if is_secret:
                result_text += '||'

        # 出力する
        print(result_text.replace('\r\n',' '))
        await message.channel.send(result_text)

# Botの起動とDiscordサーバーへの接続
f = open("config.json", 'r')
config = json.load(f)
client.run(config['discord_token'])