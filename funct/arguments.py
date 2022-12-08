def check_passwd(username, password):
    '''Функция для проверки пароля'''
    if len(password) < 8:
        print('Пароль слишком короткий')
        return False
    elif username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True


if __name__ == '__main__':
    '''Позиционные аргументы'''
    check_passwd('Nikita', '12345678')
    '''Ключевые аргументы'''
    check_passwd(username='Nikita', password='12345678')