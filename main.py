#Восьмиричные числа не превышающие 204810.
#Выводит на экран нечетные числа, использующие не менее К разных цифр.
#Список используемых цифр выводится отдельно прописью.

import re

slovar = {"0": "ноль", "1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", "7": "семь"}

file = open("text.txt", "r")
good = 0
while True:
    buffer = file.readline().split()
    if not buffer:
        print("Файл в директории проекта закончился")
        break
    print("Введите количество разных цифр")
    diff_number = int(input())
    for j in buffer:
        reg = re.findall(r"[0-7]*[0-7]", j)
        if len(reg) == 1:
            if len(j) == len(reg[0]) and len(j) <= 4:
                if int(j) % 2 != 0 and len(set(str(j))) >= diff_number and int(j, 8) <= 2048:
                    good += 1
                    print(j)
                    num = ("".join(sorted(set(j), key=j.index)))
                    for i in range(len(num)):
                        print(slovar[(num[i])], end=" ")
                    print()
if good == 0:
    print("нет подходящих чисел")

