# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 01:32:03 2017

author: Maria Zorkaltseva
"""

# Напишите программу, которая по данному числу N от 1 до 9 выводит на экран 
# N пингвинов. Изображение одного пингвина имеет размер 5×9 символов,
# между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. 
# Разрешается вывести пустой столбец после последнего пингвина. 
# Для упрощения рисования скопируйте пингвина из примера в среду разработки.

n = int(input())
print('   _~_    ' * n)
print('  (o o)   ' * n)
print(' /  V  \\  ' * n)
print('/(  _  )\\ ' * n)
print('  ^^ ^^   ' * n)
