#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> неn

N = int(input("Введите число от 1 до 7: "))
if (0 < N < 8):
    if (N == 1 or N == 2 or N == 3 or N == 4 or N == 5):
        print("no")
    else:
        print("yes")
else:
    print('такого дня нет')
