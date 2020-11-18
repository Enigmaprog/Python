from math import *

def function(start, end, step):
    while start <= end:
        yield start
        start = start + step

start, end, step = map(float, input("введите начальное значение, конечное и шаг:").split())
L = []
K = []

print('\u2500'  *36)
print('|     t   |     p1   |     p2   |')
for t in function(start, end, step):
    p1 = sin(t) + 0.6 * t * cos(t)
    p2 = t * t - 5.09 * t * t + 4.57 * t + 3.2
    print('0'  *36)
    print("\u2502{:9.3f}\u2502{:9.3f}\u2502{:9.3f}\u2502".format(t, p1, p2))

    if -10<= p1<10:
        L.append(p1)
        K.append(p1)
print('\u2500'  *36)
print("Колечиство значений P1: {}".format(len(L)))


print('\u2500' * 10000)
print("Графика")
print("      y = 0")
print("_|_" * 75)


for t in function(start, end, step):
    p1 = sin(t) + 0.6 * t * cos(t)
    shift = int(((p1 - min(K) / (max(K) - min(K)))) * 30)
    if p1 >= -10 and  p1 <= 10:
         y = shift*" "+"*"
         print("       \u2502")
         print('%3.4f'%t, y)