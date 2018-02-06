# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 00:19:42 2017

@author: Maria
"""

# Даны два списка A и B упорядоченных по неубыванию. Объедините их в один
# упорядоченный список С (то есть он должен содержать len(A)+len(B) элементов).
# Решение оформите в виде функции merge(A, B), возвращающей новый список.
# Алгоритм должен иметь сложность O(len(A)+len(B)). Модифицировать исходные
# списки запрещается. Использовать функцию sorted и метод sort запрещается.
# Формат ввода
# Программа получает на вход два неубывающих списка, каждый в отдельной строке.
# Формат вывода
# Программа должна вывести последовательность неубывающих чисел, полученных
# объединением двух данных списков.

# Тест 1
# Входные данные:
# 1 5 7
# 2 4 4 5
# Вывод программы:
# 1 2 4 4 5 5 7
#
# Тест 2
# Входные данные:
# 1 4 7
# 1 5 6
# Вывод программы:
# 1 1 4 5 6 7 
#
# Тест 3
# Входные данные:
# 1
# 1
# Вывод программы:
# 1 1

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for k in range(0, len(A) + len(B)):
    C.append(0)

i = 0
j = 0
k = 0
m = len(A)
n = len(B)

while m != 0 and n != 0:
    if A[i] <= B[j]:
        C[k] = A[i]
        i = i + 1
        m = m - 1
    else:
        C[k] = B[j]
        j = j + 1
        n = n - 1
    k = k + 1

while k < (len(A) + len(B)):
    if m == 0:
        for t in range(j, len(B)):
            C[k] = B[t]
            k = k + 1
    elif n == 0:
        for t in range(i, len(A)):
            C[k] = A[t]
            k = k + 1

print(' '.join(map(str, C)))