# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:00:36 2018

author: Maria Zorkaltseva
"""

# Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1.
# Решение оформите в виде функции MinDivisor(n). Алгоритм должен иметь
# сложность порядка корня квадратного из n.
# Указание. Если у числа n нет делителя не превосходящего корня из n,
# то число n — простое и ответом будет само число n. А у всех составных чисел
# обязательно есть делители, отличные от единицы и не превосходящие корня из n.
# Формат ввода
# Вводится натуральное число.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# 4
# Вывод программы:
# 2
#
# Тест 2
# Входные данные:
# 5
# Вывод программы:
# 5
#
# Тест 3
# Входные данные:
# 3
# Вывод программы:
# 3

def MinDivisor(n):
    i = int(n**0.5) + 1
    temp = n
    while 2 <= i <= int(n**0.5) + 1:
        div = n % i
        if div == 0:
            temp = i
        i = i - 1
    return temp

n = int(input())
print(MinDivisor(n))