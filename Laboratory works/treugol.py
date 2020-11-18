import math as m
x1,y1 = map(float,input("Введите координаты точки A:").split(" "))
x2,y2 = map(float,input("Введите координаты точки B:").split(" "))
x3,y3 = map(float,input("Введите координаты точки C:").split(" "))

def perimetr(x1, y1, x2, y2):
    l = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return (l)

l1 = perimetr(x1, y1, x2, y2)
l2 = perimetr(x2, y2, x3, y3)
l3 = perimetr(x3, y3, x1, y1)
p = (l1 + l2 + l3)/2
S = m.sqrt(p*(p-l1)*(p-l2)*(p-l3))
if (x1 == y1 and x2 == y2 and x3 == y3) or (x1 == x2 == x3) or (y1 == y2 == y3):
    print("Не треугольник")
else:
    print("Треугольник, его площадь =",int(S))


