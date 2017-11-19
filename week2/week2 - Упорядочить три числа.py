# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:09:07 2017

author: Maria Zorkaltseva
"""

# Дано три числа. Упорядочите их в порядке неубывания. Программа должна 
# считывать три числа a,b,c, затем программа должна менять их значения так, 
# чтобы стали выполнены условия a≤b≤c, затем программа выводит тройку a,b,c.
# Примечания:
# Дополнительные ограничения: нельзя использовать дополнительные переменные 
# (то есть единственной допустимой операцией присваивания является обмен 
# значений двух переменных типа (a, b) = (b, a).

A = int(input())
B = int(input())
C = int(input())
if A > B:
    (A, B) = (B, A)
if B > C:
    (B, C) = (C, B)
if B < A:
    (A, B) = (B, A)
print(A, B, C)
