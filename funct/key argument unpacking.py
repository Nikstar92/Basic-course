def check_passwd(username, password):
    '''Функция для проверки пароля'''
    if len(password) <= 7:
        print('Пароль слишком короткий')
        return False
    elif username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True


if __name__ == '__main__':
    '''Предпологаемый словарь с логинами и паролями'''
    username_passwd = [{'username': 'fallen', 'password': '1234'},
                       {'username': 'nikita', 'password': 'nikitapassword'},
                       {'username': 'Nikita', 'password': '12345678'}]
    for data in username_passwd:
        print(data)
        check_passwd(**data)