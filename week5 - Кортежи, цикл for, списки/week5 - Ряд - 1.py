# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:32:40 2018

author: Maria Zorkaltseva
"""

# Даны два целых числа A и B (при этом A≤B).
# Выведите все числа от A до B включительно.
# Формат ввода
# Вводятся два целых числа.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# 1
# 10
# Вывод программы:
# 1 2 3 4 5 6 7 8 9 10 
#
# Тест 2
# Входные данные:
# -3
# 14
# Вывод программы:
# -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 
#
# Тест 3
# Входные данные:
# 0
# 0
# Вывод программы:
# 0

A = int(input())
B = int(input())

if A <= B:
    for i in range(A, B + 1):
        print(i, end=' ')
