'''Функция для проверки пароля'''


def check_passwd(username, password):
    if len(password) <= 8:
        print('Пароль слишком короткий')
        return False
    elif username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True


'''функция add_user_to_users_file, которая запрашивает пароль для указанного пользователя,
проверяет его и запрашивает заново, если пароль не прошел проверки или
записывает пользователя и пароль в файл, если пароль прошел проверки.'''


def add_user_to_users_file(user, users_filename='users.txt', **kwargs):
    while True:
        passwd = input(f'Введите пароль для пользователя {user}:\n')
        if check_passwd(user, passwd, **kwargs):
            break
    with open(users_filename, 'a') as f:
        f.write(f'{user},{passwd}\n')


if __name__ == '__main__':
    add_user_to_users_file('nikita')
