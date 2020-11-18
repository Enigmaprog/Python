from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

d = int(input('Введите количество окружностей: '))

A = []
B = []
for i in range(d):
    x,y = map(int, input('Введите координаты центра окружности: ').split(','))
    A.append(x)
    A.append(y)
    r = int(input('Введите радиус окружности: '))
    B.append(r)
print(A)
print(B)
fig, ax = plt.subplots()
for q in range(0,len(A),2):
    for j in range(1,len(A),2):
        for k in range(len(B)):
            circle = Circle((A[q], A[j]), B[k])
            patches = [circle]
            p = PatchCollection(patches, alpha=0.01)
            ax.add_collection(p)
plt.grid(True)
plt.show()
