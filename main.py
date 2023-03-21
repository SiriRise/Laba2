#Восьмиричные числа не превышающие 2048 в десятичной системе счисления.
#Выводит на экран нечетные числа, использующие не менее 2 цифр.
#Список используемых цифр выводится отдельно прописью.

import re

slovar = {"0": "ноль", "1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", "7": "семь","-":""}

file = open("text.txt", "r")
while True:
    buffer = file.readline().split()
    if not buffer:
        print('Файл пуст')
        break
    good = 0
    for j in buffer:
        reg = re.findall(r'^-?(-[0-7]+[1357]|^-?[0-7][1357]|^-?[0-7][0-7][1357]|^-?[0-3][0-7][0-7][1357])\b', j)
        if len(reg) == 1:
                good = 1
                print(''.join(reg))
                num = ("".join(sorted(set(j), key=j.index)))
                for i in range(len(num)):
                    print(slovar[(num[i])], end=" ")
                print()
    if good == 0:
        print("нет подходящих чисел")
    break
