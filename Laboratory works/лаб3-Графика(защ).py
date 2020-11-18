from math import *


def function(start, end, step):
    while start<=end:
        yield start
        start +=step


start, end, step = map(float, input("введите начаьное значение, конечное и шаг:").split())
L=[]
K=[]
print('\u2500'  *36)
print('|     x   |     y   |')


for x in function(start, end, step):
    y = cos(x / 2) - 4
    print('\u2500' * 36)
    print("\u2502{:9.3f}\u2502{:9.3f}".format(x, y))
    if 0.2 <= y <= 1.6:
        L.append(y)
    K.append(y)


print('\u2500' * 25)
print("Колечиство значений y: {}".format(len(L)))
print('\u2500' * 10000)
print("Графика")
print("                                y = 0")
print("_|_" * 75)
for x in function(start, end, step):
    y = cos(x/2)-4
    #shift = int((max(K) - min(K))/75*(y - min(K)))
    shift = int(((y - min(K) / (max(K) - min(K)))) * 30)
    if y >= 0.2 and  y <= 1.6:
        y = shift*" "+"*"
        print("                                  \u2502")
        print('%3.4f'%x, y)








