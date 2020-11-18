from math import *
x1, y1 = map(int, input("Введите координату точки А").split(','))
x2, y2 = map(int, input("Введите координату точки B").split(','))
x3, y3 = map(int, input("Введите координату точки C").split(','))
AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
BC = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
CA = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
if AB < BC + CA and BC < CA + AB and CA < AB + BC:
    r = min(AB, BC, CA)       # r- наименьшая сторона треугольника
    if r == AB:               # m1,n1 - координаты медианы треугольника
        m1 = (x1 + x2) / 2    # g - длина медианы
        n1 = (y1 + y2) / 2
        g = sqrt((m1 - x3) ** 2 + (n1 - y3) ** 2)
        print("Медиана, проведеная из ниаменьшего угла : {:5.3f}".format(g))
    elif r == BC:
        m1 = (x3+x2)/2
        n1 = (y3+y2)/2
        x = sqrt ((m1-x1) ** 2 + (n1-y1) ** 2)
        print("Медиана, проведеная из ниаменьшего угла : {:5.3f}".format(x))
    else:
        m1 = (x1+x3)/2
        n1 = (y1+y3)/2
        x = sqrt ((m1-x2) ** 2 + (n1-y2) ** 2)
        print ("Медиана, проведеная из ниаменьшего угла : {:5.3f}".format(x))
else:
    print("Не треугольник")
