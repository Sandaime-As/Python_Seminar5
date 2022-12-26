# 1. Создайте программу для игры с конфетами человек против человека.
# * Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

import random

candies = 117
FirstMove = random.random()
moves = ['Ход Игрока', 'Ход Бота']
if FirstMove > 0.5:
    print('Первым ходит Игрок')
else:
    moves.sort()
    print('Первым ходит Бот')
player = 0
while candies > 0:
    print(moves[player])
    if moves[player] == 'Ход бота':
        count = random.randint(1, 28)
        print(f'Бот взял {count} конфет')
    else:
        count = int(input('Сколько конфет возмёте?  '))
    if 0 < count < 29 and not (count > candies):
        candies -= count
        if candies <= 0:
            print(f'Конфет не осталось!')
            if len(moves[player]) == 8:
                print('Победил Бот!')
            else:
                print(f'Победил Игрок {moves[player][11:]}')
        else:
            print(f'Осталось {candies} конфет')
            player = (player + 1) % 2
    else:
        print('Ход не по правилам')
