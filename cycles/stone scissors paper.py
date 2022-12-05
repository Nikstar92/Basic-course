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

