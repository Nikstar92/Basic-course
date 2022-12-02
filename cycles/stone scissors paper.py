import random
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
                break
