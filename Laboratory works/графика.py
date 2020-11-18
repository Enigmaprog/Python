from math import sin, pi, floor

start = float(input('start= '))
end = float(input('end= '))
step = float(input('step= '))
screen_width = 80

numbers_of_iteration = floor((end-start) / step) + 1

print('_' * 42)
print('|x' + ' '*11 + '|y1' + ' ' * 11 + '|y2' + ' ' * 11 + "|y3" + " " * 11 +'|')
print('_' * 42)

start_copy = start
while start < end:
    start += step
    x = start
    y1 = x**3 - 10.2*x**2 - 91.2*x + 492.6
    y2 = x - 1.2**x
    y3 = y1 + y2/2
    print("|{:12g}|{:13g}|{:13g}|{:13g}|".format(x, y1, y2, y3))
print('_'*42)

x = start
miny1 = maxy1 = x**3 - 10.2*x**2 - 91.2*x + 492.6
miny2 = maxy2 = x - 1.2**x
miny3 = maxy3 = y1 + y2/2



start = start_copy
while start<end:
    start += step
    x = start
    y1 = x**3 - 10.2*x**2 - 91.2*x + 492.6
    y2 = x - 1.2**x
    y3 = y1 + y2/2
    if y1 < miny1:
        miny1 = y1
    if y2 < miny2:
        miny2 = y2
    if y3 < miny3:
        miny3 = y3
    if y1 > maxy1:
        maxy1 = y1
    if y2 > maxy2:
        maxy2 = y2
    if y3 > maxy3:
        maxy3 = y3