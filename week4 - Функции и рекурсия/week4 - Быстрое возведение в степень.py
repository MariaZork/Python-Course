# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:08:06 2018

author: Maria Zorkaltseva
"""

# Возводить в степень можно гораздо быстрее, чем за n умножений!
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
# aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n. Реализуйте алгоритм
# быстрого возведения в степень. Если вы все сделаете правильно,то
# сложность вашего алгоритма будет O(logn).
# Формат ввода
# Вводится действительное число a и целое число n.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# 2
# 1
# Вывод программы:
# 2
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
# 3
# Вывод программы:
# 8

def pow(a, n):
    if n % 2 == 0:
        return (a**2)**(n/2)
    if n % 2 != 0:
        return a*pow(a, n-1)
    return a

a = float(input())
n = int(input())
print(pow(a, n))