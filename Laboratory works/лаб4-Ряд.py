global eps
eps = float(input('eps='))
global maxN
maxN = int(input('maxN='))
x = float(input('x='))

def my_exp(x):
    s=1
    q=1
    n=1
    while abs(eps)<=abs(q) and maxN >= n:
        q *= x/n
        s += q
        n+=1
    return s
result=my_exp(x)
print('Sum= {}'.format(result))