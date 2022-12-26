# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи

def getNegaFib(count):
    if count == 0:
        return [0]

    fibArray = [1, 0, 1]

    for i in range(1, count):
        fibArray.append(fibArray[len(fibArray) - 1] +
                        fibArray[len(fibArray) - 2])
        fibArray.insert(0, fibArray[1] - fibArray[0])

    return fibArray


number = int(input('Введите k '))
print(getNegaFib(number))
