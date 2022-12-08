def sum_kwarg(**kwargs):
    '''Функция подсчета суммы с ключевым аргументом переменной длины'''
    print(kwargs)
    return sum(kwargs.values())


if __name__ == '__main__':
    print(sum_kwarg(a=1, b=2, c=3, d=4, e=5))
