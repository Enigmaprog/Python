from math import log

global x
x = float(input("Введите x:"))
global eps
eps = float(input("Введите точность (eps): "))
global Nmax
Nmax = int(input("Введите количество итераций: "))
global step
step = int(input("Введите шаг"))
global A
def my_exp(x):
    global A
    q = x / 20
    s = log(5 / 4) + q
    k = 2
    while abs(eps) <= abs(q) and Nmax >= k:
        q = x ** k / k * (1 / 4 ** k - 1 / 5 ** k)
        k += 1
        s += q
    return s
result = my_exp(x)
print("Sum={} ".format(result))
