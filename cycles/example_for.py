# вывод звездочек
i = int(input('Введите число = '))
for a in range(i):
    print('*' * (a + 1))
#вывод четных и нечетных
i = int(input('Введите число = '))
for a in range(i + 1):
    if a % 2 == 0:
        print(f'{a} is EVEN')
    else:
        print(f'{a} is ODD')
# сумму всех чисел, делимых без остатка на 3 и на 5. Вывести на консоль это число.
summa = 0
a = int(input('введите число = '))
for b in range(a + 1):
    if b % 3 == 0 or b % 5 == 0:
        print(b)
        summa += b
    else:
        pass
print(f"Сумма чисел = {summa}")
# два списка, из первого берем нечетные, из второго четные и складываем
list1 = []
first_list = [1, 2, 4, 12, 54, 43, 6, 9, 10]
for i in first_list:
    if i % 2 != 0:
        list1.append(i)
print(list1)

list2 = []
second_list = [3, 2, 4, 9, 92, 15, 43, 2, 55]
for i in second_list:
    if i % 2 == 0:
        list2.append(i)
print(list2)
list3 = list1 + list2
print(list3)

# список карт
current_hand = [2, 3, 4, 10, 'Q', 5]
# 2,3,4,5,6 весят + 1
# 7, 8, 9 весят 0
# 10, 'J', 'Q', 'K', 'A' весят -1
cards = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
cards_sum = sum([cards[x] for x in current_hand])
print(f'сумма карт на руке = {cards_sum}')
