# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих 
# на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def CreateRndList(countElements, maxElement):
    listElements = []
    for i in range(countElements):
        listElements.append(random.randint(0,maxElement))
    return listElements

myList = CreateRndList(6, 30)
sum = 0
elements = []

for i in range(len(myList)):
    if i % 2 != 0:
        elements.append(myList[i])
        sum += myList[i]

print(myList)

if len(elements) == 0:
    print("Нет элементов удовлетвоярющих условию")
else: 
    print(f'На нечётных позициях элементы {elements}, ответ: {sum}')

