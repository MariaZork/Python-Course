# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:09:46 2018

author: Maria Zorkaltseva
"""

# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа p и q таких,
# что (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m), получающая значения
# n и m и возвращающей кортеж из двух чисел (return p, q).
# Формат ввода
# Вводятся два натуральных числа.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# 12
# 16
# Вывод программы:
# 3 4
#
# Тест 2
# Входные данные:
# 7
# 9
# Вывод программы:
# 7 9
#
# Тест 3
# Входные данные:
# 10
# 100
# Вывод программы:
# 1 10

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def ReduceFraction(n, m):
    x = gcd(n, m)
    p = n // x
    q = m // x
    return p, q

n = int(input())
m = int(input())
p, q = ReduceFraction(n, m)
print(p, q)