# -*- cording:utf-8 -*-

import random
import subprocess
import time

from colorama import Fore, Back, Style

# 変数セット
hand = ('グー','チョキ','パー')
result = ('> 勝ち！','> 負け...',"> あいこ")
trainer = ('エリートトレーナー','ドクター','たんパンこぞう','おまわりさん')

beforeSerif = (
  'おおぜいの 中から ぼくに 話しかけた きみ！ みる 目 あるじゃないか！',
  'ドクター！ おきゃくさま 中に ドクターは いませんか？ \n はい わたしが ドクターです さっそく 勝負と まいりましょう',
  'オレが はいているのは たんぱん じゃない！ ハーフパンツ なんだよ！',
  'おまえが　犯人かーっ！',
)
afterSerif = (
  'めのまえが まっくらに なった!',
  'まだまだ しょうぶは これからだ！'
  )
afterWin = (
  'すごい 手応えだ！ いい　勝負が　できたよ',
  'あれれれ…… ひさしぶりすぎて カンが にぶったかな？',
  'オマエ 強すぎるから たんぱん ずりおちそうに なっただろ！ おまえ すげーなー！',
  '犯人じゃ なかったね…… ごめん！ ソーリー！',
  )


trInt = random.randint(0,3)
print(f'{trainer[trInt]}が しょうぶを しかけてきた！')
print(f'{Fore.CYAN} {trainer[trInt]}『{beforeSerif[trInt]}』{Fore.RESET}')

while True:

  print(f' > 0.{hand[0]} \n > 1.{hand[1]} \n > 2.{hand[2]}')
  user = input('あなたは どうする？：')


  # 入力チェック
  uInt = int(user) if user.isdecimal() else {print(f'{Fore.RED} {trainer[trInt]}『 数字を 入力しよう！』{Fore.RESET}'),exit()}
  if uInt < 3:
    print(f'あなたは {Fore.CYAN}{hand[uInt]}{Fore.RESET}を 出した')
  else:
    print(f'{Fore.RED} {trainer[trInt]}『 0 から 2 の 数字を 入力しよう！』{Fore.RESET}')
    exit()


  print('じゃんけん　ポンッ！')
  cpInt = random.randint(0,2)

  # 判定
  if uInt - cpInt == 0:
    print(f'{trainer[trInt]}は {Fore.CYAN}{hand[cpInt]}{Fore.RESET}を 出した')
    print(f'{Fore.CYAN}{result[2]}{Fore.RESET}')
    print(f'{Fore.CYAN} {trainer[trInt]}『{afterSerif[1]}』{Fore.RESET}')  

  elif uInt - cpInt == 1 or uInt - cpInt == 2:
    print(f'{trainer[trInt]}は {Fore.CYAN}{hand[cpInt]}{Fore.RESET}を 出した')
    print(f'{Fore.GREEN}{result[0]}')
    print(f'{trainer[trInt]}『{afterWin[trInt]}』{Fore.RESET}')
    break

  else:
    print(f'{trainer[trInt]}は {Fore.CYAN}{hand[cpInt]}{Fore.RESET}を 出した')
    print(f'{Style.DIM} {Fore.RED}{result[1]}')
    print(f'『{afterSerif[0]}』{Style.RESET_ALL}')
    time.sleep(0.5)
    subprocess.call(['clear'])
    break