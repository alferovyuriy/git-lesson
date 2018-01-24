'''
Условие
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции. 
'''
from math import sqrt

def distance():
    dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist
    
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance())