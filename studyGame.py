# -*- cording:utf-8 -*-

# random関数のモジュール
import random
from colorama import Fore, Back, Style

hand = ('グー','チョキ','パー')
result = ('> 勝ち！','> 負け！',"> あいこ！")
trainer = ('エリートトレーナー','ドクター','たんパンこぞう')

beforeSerif = (
  'おおぜいの 中から ぼくに 話しかけた きみ！ みる 目 あるじゃないか！',
  'ドクター！ おきゃくさま 中に ドクターは いませんか？ \n はい わたしが ドクターです さっそく 勝負と まいりましょう',
  'オレが はいているのは たんぱん じゃない！ ハーフパンツ なんだよ！',
)
afterSerif = (
  '負けた　勝負も　ホロ苦い　思い出だ……',
  'めのまえが まっくらに なった!',
  'まだまだ しょうぶは これからだ！'
  )

trInt = random.randint(0,2)

# 変数と文字列の結合は、f文字列を使用する
print(f'{trainer[trInt]}が しょうぶを しかけてきた！')
print(f'{Fore.CYAN} {trainer[trInt]}『{beforeSerif[trInt]}』{Fore.RESET}')


print(f' > 0.{hand[0]} \n > 1.{hand[1]} \n > 2.{hand[2]}')

user = input('あなたは どうする？：')
uInt = int(user)
cpInt = random.randint(0,2)

print('じゃんけん　ポンッ！')


if uInt < 3:
  print(f'あなた：{Fore.CYAN} {hand[uInt]} {Fore.RESET}を 出した')
else:
  print(f'{Fore.RED} > 1 から 3 の 数字を 入力して じゃんけん しよう！{Fore.RESET}')
  exit()


if uInt - cpInt == 0:
  print(f'{trainer[trInt]}は {Fore.CYAN} {hand[cpInt]} {Fore.RESET}を 出した')
  print(f'{Fore.CYAN}{result[2]}{Fore.RESET}')
  print(f'{Fore.CYAN} {trainer[trInt]}『{afterSerif[2]}』{Fore.RESET}')
  
elif uInt - cpInt == 1 or uInt - cpInt == 2:
  print(f'{trainer[trInt]}は {Fore.CYAN} {hand[cpInt]} {Fore.RESET}を 出した')
  print(f'{Fore.GREEN}{result[0]}')
  print(f'{trainer[trInt]}『{afterSerif[0]}』{Fore.RESET}')
  
else:
  print(f'{trainer[trInt]}は {Fore.CYAN} {hand[cpInt]} {Fore.RESET}を 出した')
  print(f'{Style.DIM} {Fore.RED}{result[1]}')
  print(f'『{afterSerif[1]}』{Style.RESET_ALL}')