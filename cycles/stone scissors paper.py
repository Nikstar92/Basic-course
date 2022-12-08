"""
Написать игру в "камень-ножницы-бумага" против компьютера.
Запустить игру в бесконечном цикле. Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага).
Сгенерировать случайный выбор компьютера. Вывести выбор компьютера. Определить победителя, выведя соответствующую
информацию. Спросить пользователя - хочет ли он повторить игру. Если хочет - повторить, не хочет - выйти из цикла.
"""

import random
import sys

WIN = "Вы выиграли"
DRAW = "Ничья"
LOSE = "Вы проиграли"
ITEMS = {
    "r": {
        "r": DRAW, "s": LOSE, "p": WIN
    },
    "s": {
        "r": WIN, "s": DRAW, "p": LOSE
    },
    'p': {
        "r": LOSE, "s": WIN, "p": DRAW
    }
}
items = ['R', 'S', 'P']
user_answer = input('Хотите поиграть? Y/N\n').lower()
if user_answer != 'y':
    sys.exit()
while True:
    comp = random.choice(items).lower()
    u_answer = input('Что вы ставите? R - камень, S - ножницы, P - бумага\n').lower()
    print(comp.upper())
    print(ITEMS[comp][u_answer])
    repeat = input("Хотите повторить? Y/N\n").lower()
    if repeat != 'y':
        break

'''Или так, длинее, но по шагово'''
'''import random
items = ['R', 'S', 'P']
comp = random.choice(items).lower()
user_answer = input('Хотите поиграть? Y/N\n').lower()
if user_answer == 'y':
    while True:
        u_answer = input('Что вы ставите? R - камень, S - ножницы, P - бумага\n').lower()
        print(comp)
        if comp == 'r' and u_answer == 's' or comp == 's' and u_answer == 'p' or comp == 'p' and u_answer == 'r':
            print('Вы проиграли')
            user = input("Хотите повторить? Y/N\n").lower()
            if user == 'y':
                comp = random.choice(items).lower()
                continue
            else:
                break
        elif comp == 'r' and u_answer == 'p' or comp == 's' and u_answer == 'r' or comp == 'p' and u_answer == 's':
            print('Вы выиграли')
            user = input("Хотите повторить? Y/N\n").lower()
            if user == 'y':
                comp = random.choice(items).lower()
                continue
            else:
                break
        else:
            print('Ничья')
            user = input("Хотите повторить? Y/N\n").lower()
            if user == 'y':
                comp = random.choice(items).lower()
                continue
            else:
                break'''