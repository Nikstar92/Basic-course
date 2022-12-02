user_number = int(input('Число = '))
reversed_number = 0
original_number = user_number
while original_number > 0:
    # добавляем разряд умножая на 10 и добавляем последний разряд из исходного числа
    reversed_number = (reversed_number * 10) + original_number % 10
    # откусываем последний разряд и перезависываем число
    original_number = original_number // 10

if user_number == reversed_number:
    print('palindrome')
else:
    print('no palindrome')