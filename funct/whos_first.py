'''Два участника p1 и p2 участвуют в дуэли.
Напишите функцию whos_first, которая принимает две строки и возвращает имя игрока, который выстрелил первым.
Если игроки выстрелили одновременно, то вернуть строку "tie".'''


def whos_first(p1, p2):
    p1 = p1.rstrip()
    p2 = p2.rstrip()
    if len(p2) < len(p1):
        print('p2')
    elif len(p1) < len(p2):
        print('p1')
    else:
        print('tie')


whos_first('   Bang! ', ' Bang!        ')

'''или можно так решить'''


def shutdown(p1, p2):
    diff = p1.find('B') - p2.find('B')
    if diff < 0:
        return 'p1'
    elif diff > 0:
        return 'p2'
    else:
        'tie'


print(shutdown('    Bang!  ', ' Bang!    '))
