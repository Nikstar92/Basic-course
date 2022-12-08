def sum_arg(*args):
    '''Функция подсчета суммы с позиционным аргументом переменной длины'''
    print(args)
    return sum(args)


if __name__ == '__main__':
    print(sum_arg(1, 2, 3, 4, 5))
