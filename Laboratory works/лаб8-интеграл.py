def f(x):
    return x * x


def simpson(N, delta):
    N *= 2
    delta /= 2
    k = 2
    i = a + delta
    res = f(a) + f(b)
    while i <= b - delta + 1e-5:
        if k % 2 == 0:
            res += 4 * f(i)
        else:
            res += 2 * f(i)

        i += delta
        k += 1
    res *= (b - a) / 3 / N
    return res


def trapec(N, delta):
    i = a + delta
    res = (f(a) + f(b)) / 2
    while i <= b - delta + 1e-9:
        res += f(i)
        i += delta
    res *= delta

    return res


def srednPrqm(N, delta):
    res = 0
    i = a
    while i <= b:
        res += f(i + delta / 2) * delta
        i += delta
    return res


def toIncreasePrecisionSimp(N, delta):
    res = 1
    while abs(simpson(N, delta) - simpson(N * 2, delta / 2)) > abs(eps):
        delta /= 2
        N *= 2
        res *= 2

    return res


def toIncreasePrecisionTrap(N, delta):
    res = 1
    while abs(trapec(N, delta) - trapec(N * 2, delta / 2)) > abs(eps):
        delta /= 2
        N *= 2
        res *= 2

    return res


def toIncreasePrecisionSrTrap(N, delta):
    res = 1
    while abs(srednPrqm(N, delta) - srednPrqm(N * 2, delta / 2)) > abs(eps):
        delta /= 2
        N *= 2
        res *= 2

    return res


print("Interval:")
a = float(input("a = "))
b = float(input("b = "))
if a > b: a, b = b, a

N1 = float(input("N1 = "))
N2 = float(input("N2 = "))
delta1 = (b - a) / N1
delta2 = (b - a) / N2
eps = float(input("eps = "))

sum = [[], [], []]
precision = toIncreasePrecisionTrap(N1, delta1)
N = N1 * precision
delta = delta1 / precision
sum[0].append([trapec(N, delta), N])

precision = toIncreasePrecisionTrap(N2, delta2)
N = N2 * precision
delta = delta2 / precision
sum[0].append([trapec(N, delta), N])

precision = toIncreasePrecisionSimp(N1, delta1)
N = N1 * precision
delta = delta1 / precision
sum[1].append([simpson(N, delta), N])

precision = toIncreasePrecisionSimp(N2, delta2)
N = N2 * precision
delta = delta2 / precision
sum[1].append([simpson(N, delta), N])

precision = toIncreasePrecisionSrTrap(N1, delta1)
N = N1 * precision
delta = delta1 / precision
sum[2].append([simpson(N, delta), N])

precision = toIncreasePrecisionSrTrap(N2, delta2)
N = N2 * precision
delta = delta2 / precision
sum[2].append([simpson(N, delta), N])

print("-" * 56)
print("|" + " " * 10 + "|" + " " + "{:^19}".format(N1) + " " + "|" + " " + "{:^19}".format(N2) + " " + "|")
print("-" * 56)
print("|" + " Трапеций " + "|" + " {:^10.6}: {:7.0f} ".format(sum[0][0][0],
                                                              sum[0][0][1]) + "|" + " {:^10.6}: {:7.0f} ".format(
    sum[0][1][0], sum[0][1][1]) + "|")
print("-" * 56)
print("|" + " Симпсона " + "|" + " {:^10.6}: {:7.0f} ".format(sum[1][0][0],
                                                              sum[1][0][1]) + "|" + " {:^10.6}: {:7.0f} ".format(
    sum[1][1][0], sum[1][1][1]) + "|")
print("-" * 56)
print("|" + " Ср. трап " + "|" + " {:^10.6}: {:7.0f} ".format(sum[2][0][0],
                                                              sum[2][0][1]) + "|" + " {:^10.6}: {:7.0f} ".format(
    sum[2][1][0], sum[2][1][1]) + "|")
print("-" * 56)