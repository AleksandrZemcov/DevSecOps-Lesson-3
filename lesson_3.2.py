"""Вывести все простые числа от 2 до 100"""

num = 2
while num <= 100:
    prime_number = True
    divisor = 2

    while divisor * divisor <= num:
        if num % divisor == 0:
            prime_number = False
            break
        divisor += 1

    if prime_number:
        print(num, end=" ")

    num += 1
