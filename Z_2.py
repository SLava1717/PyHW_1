#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input("Задайте значение X: "))
Y = int(input("Задайте значение Y: "))
Z = int(input("Задайте значение Z: "))
if (not(X or Y or Z) == (not X and not Y and not Z)):
    print('True')
else:
    print('False')
