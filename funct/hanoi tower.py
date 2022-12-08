def solve_hanoi_tower(discs):
    return (2 ** discs) - 1


if __name__ == '__main__':
    n = int(input('Сколько дисков?\n'))
    if n > 0:
        print(solve_hanoi_tower(n))
    else:
        print('Введите положительное число.')
