import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def linear_regression(start, stop, ys, xs=None, xlab='x', ylab='y'):     # x,y = list  len(x)=len(y)
    if xs:
        x = np.array(xs)
    else:
        x = np.arange(start, stop, step=(stop-start)/len(ys))

    y = np.array(ys)

    x_bar = np.mean(x)
    y_bar = np.mean(y)
    print(f'mean x = {x_bar}, mean y = {y_bar}')
    b1 = sum((x - x_bar)*(y - y_bar))/sum((x - x_bar)**2)
    b0 = y_bar - b1*x_bar

    y_hat = b0 + b1*x

    print(f'k = {b1}, m = {b0}')
    print(f'Värde = {b1-b0}')
    plt.scatter(x, y)
    plt.grid()
    plt.plot(x, y_hat)
    plt.plot(x_bar, y_bar, 'ro')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.show()

    return x, y_hat



