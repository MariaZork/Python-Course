# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 23:45:31 2017

author: Maria Zorkaltseva
"""

# Дано положительное действительное число X. Выведите его дробную часть.
# Формат ввода
# Вводятся положительное действительное число.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# 17.9
# Вывод программы:
# 0.9
#
# Тест 2
# Входные данные:
# 10.34
# Вывод программы:
# 0.34
#
# Тест 3
# Входные данные:
# 0.001
# Вывод программы:
# 0.001

X = float(input())
diff = X - int(X)
print('{0:.3f}'.format(diff))