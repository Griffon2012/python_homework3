# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
import math

def CreateRndList(countElements, maxElement):
    listElements = []
    for i in range(countElements):
        listElements.append(random.randint(0,maxElement))
    return listElements

randomList = CreateRndList(6, 10)
resultList = []
print(randomList)

for i in range(math.ceil(len(randomList) / 2)):
    resultList.append(randomList[i] * randomList[-i - 1])
print(resultList)