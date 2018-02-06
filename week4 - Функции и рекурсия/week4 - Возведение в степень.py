# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:04:39 2018

author: Maria Zorkaltseva
"""

# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите aⁿ не используя циклы и стандартную функцию pow,
# а используя рекуррентное соотношение aⁿ=a⋅aⁿ⁻¹.
# Решение оформите в виде функции power(a, n).
# Формат ввода
# Вводятся действительное положительное число a и целое неотрицательное число n
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# 2
# 3
# Вывод программы:
# 8
#
# Тест 2
# Входные данные:
# 2
# 2
# Вывод программы:
# 4
#
# Тест 3
# Входные данные:
# 2
# 1
# Вывод программы:
# 2

def power(a, n):
    if n > 0:
        return a*power(a, n - 1)
    return 1

a = float(input())
n = int(input())
print(power(a, n))