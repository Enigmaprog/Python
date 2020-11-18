from math import *

a,b,c =map (float, input("Введите число:").split())
if a==0:
    if b==0:
        if c==0:
            print("Безконечное количество корней")
        else:
            print("Корней нет")
    else:
        x = -c/b
        print(" x = {:0.2f}".format(x))
else:
    d = b*b-4*a*c
    if d<0:
        print("нет корней")
    elif d==0:
        x = - b/ (2*a)
        print(" x = {:0.2f}".format(x))
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print(" x1 = {:0.2f} x2 = {:1.2f}".format(x1, x2))