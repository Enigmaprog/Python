#ИУ7-16N
#Лабораторная работа
#Батбилэг Номуундалай
from math import *
x1, y1 = map(int, input("Введите координату точки А").split(','))
x2, y2 = map(int, input("Введите координату точки B").split(','))
x3, y3 = map(int, input("Введите координату точки C").split(','))
AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
BC = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
CA = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
if AB < BC + CA and BC < CA + AB and CA < AB + BC:
    print("Длина первой стороны: {:5.3f}". format(AB))
    print("Длина второй стороны: {:5.3f}". format(BC))
    print("Длина третей стороны: {:5.3f}" . format(CA))

    r = max(AB,BC,CA)                  # r- наибольшая сторона треугольника
    if r == AB:                        # m1,n1 - координаты медианы треугольника
        m1 = (x1+x2)/2                 # g - длина медианы
        n1 = (y1+y2)/2
        g = sqrt ((m1-x3) ** 2 + (n1-y3) ** 2)
        print ("Медиана, проведеная из ниабольшего угла : {:5.3f}" .format(g))
    elif r == BC:
        m1 = (x3+x2)/2
        n1 = (y3+y2)/2
        x = sqrt ((m1-x1) ** 2 + (n1-y1) ** 2)
        print("Медиана, проведеная из ниабольшего угла : {:5.3f}".format(x))
    else:
        m1 = (x1+x3)/2
        n1 = (y1+y3)/2
        x = sqrt ((m1-x2) ** 2 + (n1-y2) ** 2)
        print ("Медиан, проведеная из ниабольшего угла : {:5.3f}".format(x))
# Ввод произвольной точки
    m2, n2 = map(int, input("Введите координаты произвольной точки : ").split(','))

# Определение принадлежность точки треуголнику
# i,o,p - временные переменные
    i = (x1 - m2) * (y2 - y1) - (x2 - x1) * (y1 - n2)
    o = (x2 - m2) * (y3 - y2) - (x3 - x2) * (y2 - n2)
    p = (x3 - m2) * (y1 - y3) - (x1 - x3) * (y3 - n2)

    if i == 0 or o == 0 or p == 0 :
        print("Точка лежит на стороне треугольника" )
    elif i == abs(i) and o == abs(o) and p == abs(p)\
        or -i == abs(i) and -o == abs(o) and -p == abs(p):
        print("Точка принадлежит треугольнику")

        AL = sqrt((m2-x1)**2+(n2-y1)**2)
        BL = sqrt((m2-x2)**2+(n2-y2)**2)
        CL = sqrt((m2-x3)**2+(n2-y3)**2)
        p1 = (AL+CL+CA)/2
        p2 = (AB+AL+BL)/2
        p3 =(CL+BL+BC)/2
        s1 = sqrt(p1*(p1-AL)*(p1-CL)*(p1-CA))
        s2 = sqrt(p2*(p2-AB)*(p2-AL)*(p2-BL))
        s3 = sqrt(p3*(p3-CL)*(p3-BL)*(p3-BC))
        RL = 2 * s2 / AB
        TL = 2 * s3 / BC
        SL = 2 * s1 / CA
        h = min(RL,TL,SL)
        print("Расстояние от произвольной точки до наиболее стороны: {:9.5f}".format(h))
    else:
        print("Точка не принадлежит треугольнику")
else:
    print("Не треугольник")