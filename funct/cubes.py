def calc_dice_scores(lst):
    return sum([a + b for a, b in lst]) if not any(a == b for a, b in lst) else 0


if __name__ == '__main__':
    print(calc_dice_scores([(1, 4), (3, 4), (5, 6)]))
