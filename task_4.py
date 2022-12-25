# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def toBinary(number):
    result = ''
    remainder = None

    while True:
        if number % 2 > 0:
            remainder = 1
        else:
            remainder = 0
        number //= 2
        result = str(remainder) + result
        if number == 1:
            result = str(number) + result
            break
    return result

number = int(input('Введите десятичное число: '))

print(toBinary(number))
