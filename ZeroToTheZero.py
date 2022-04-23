import matplotlib.pyplot as plt
from decimal import *
from dubbleBubbleSort import dbs

LowerBound = []
results = []
ns = []
nDecimals = 5
getcontext().prec = nDecimals
ZeroStr = '0'


def ZeroZero(nDecimals):

    delta = Decimal('0.{}1'.format(ZeroStr * (nDecimals - 1)))
    prev = 1
    smallest = 1
    n = delta
    i = 1


    while n <= 1 - delta:
        result = Decimal(pow(n, n))
        results.append(result)
        ns.append(n)
        print(f'delta = {delta}      n = {n}     result = {result}')
        if result > prev:
            if smallest > prev:
                smallest = prev
            LowerBound.append(prev)

        prev = result
        i += 1
        n += delta
    print(sorted(LowerBound))

    plt.plot(ns, results, 'r-')
    plt.show()

    dbsorted = dbs(ns, results)

    x = []
    y = []

    for n, r in dbsorted:
        x.append(n)
        y.append(r)
        print(f'sorted N = {n}     sorted R = {r}')



if __name__ == '__main__':
    ZeroZero(nDecimals)









