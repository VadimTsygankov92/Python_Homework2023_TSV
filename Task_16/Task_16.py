# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 3
# -> 1


n = int(input("Введите длину массива: "))
a = [int(input(f"Введите {i+1}-е число: ")) for i in range(n)]
x = int(input("Введите число для поиска: "))
print(f"В массиве число {x} встречается: {a.count(x)} раз(а)")