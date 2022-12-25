# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random


def CreateRndList(countElements, maxElement):
    listElements = []
    for i in range(countElements):
        randElement = random.random() * maxElement
        listElements.append(round(random.random() * maxElement, 2))
    return listElements


myList = CreateRndList(5, 10)

min = None
max = None

for i in myList:
    if int(i) != i:
        fractionalPart = round(i - int(i), 2)
        if min is None or max is None:
            max = min = fractionalPart
        if min > fractionalPart:
            min = fractionalPart
        if max < fractionalPart:
            max = fractionalPart

diff = round(max - min, 2)
print(myList)
print(diff)
