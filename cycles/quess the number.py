import random
comp_number = random.randint(1, 50)
count = 6
while count != 0:
    user_number = int(input('Введите число от 1 до 50 = '))
    if comp_number > user_number:
        print(f'Ваше число меньше загаданого! попыток осталось {count -1}')
    elif comp_number < user_number:
        print(f'Ваше число больше загаданого! попыток осталось {count - 1}')
    elif comp_number == user_number:
        print('Вы угадали')
        break
    if comp_number != user_number and count == 1:
        print(f'Вы проиграли, правильный ответ {comp_number}')
    count -= 1
