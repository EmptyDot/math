import math
import numpy as np
import sys
from sympy import symbols, limit
from typing import Union

def get_factors(n):  # n = int
    """Returns the factors of n"""

    factors = [i for i in range(2, n-1) if n % i == 0]
    if factors:
        print(f'Factors of {n}: {factors}')
        return factors  # list
    else:
        print(f'{n} is prime!')
        return


def get_common_factors(n, m) -> list:  # n,m = int
    """Returns the common factors of n and m"""
    common = []


    nfactors = get_factors(n)
    mfactors = get_factors(m)
    if nfactors and mfactors:
        common = [k for k in range(2, min(n, m) + 1) if k in nfactors and k in mfactors]
    else:
        print(f'{n} and/or {m} is prime.')
        return common

    if common:
        print(f'Common factors: {common}')
        print(f'{n} / {m} = {n / m}')
        print(f'{n} / {common[-1]} = {int(n / common[-1])}')
        print(f'{m} / {common[-1]} = {int(m / common[-1])}')
    else:
        print(f'No common factors of {n} and {m}')
    return common  # list or None


def hasFactors(n, m):  # n,m = int
    """Returns the values that can be factored into n and m up to n*m + 1"""
    value = [i for i in range(2, n*m + 1) if i % n == 0 and i % m == 0]
    return value


def felmarginal(p, n, prec=1.96):
    return prec * np.sqrt((p * (100-p))/n)


def medelvarde(nums):       # nums = list
    return sum(nums)/len(nums)


def standardavvikelse(nums):
    k = 0
    a = 0
    x = medelvarde(nums)
    for i in nums:
        k += pow(i - x, 2)
        a += i - x

    return np.sqrt(k / (len(nums) - 1))


def binomial_coefficient(n, k):  # n = size of a given set, k = size of the subset
    """Return number of ways to choose an (unordered) subset of k elements from a fixed set of n elements"""
    value = (math.factorial(n))/(math.factorial(n - k) * math.factorial(k))
    return int(value)


def expand_binomial_power(n, sign, a='a', b='b'):  # n = int  a,b = str, int, float  sign = '+' or '-'
    """Expands the expression (a+b)**n or (a-b)**n. Returns a string of the expansion."""

    string = ''
    for k in range(n + 1):
        bc = binomial_coefficient(n, k)

        if n-k == 0:
            a_term = False
        elif n-k == 1:
            a_term = f'{a}'
        elif n-k == -1:
            a_term = f'-{a}'
        else:
            a_term = f'{a}**{n-k}'
        if k == 0:
            b_term = False
        elif k == 1:
            b_term = f'{b}'
        elif k == -1:
            b_term = f'(-{b})'
        else:
            b_term = f'{b}**{k}'

        if bc == 1:
            pass
        elif bc > 1 or bc < -1:
            string += str(bc)
            if a_term and str(a) in '0123456789':
                string += '*'
        if a_term:
            string += a_term
            if b_term:
                string += '*'
        if b_term:
            if sign == '-':
                b_term = f'(-{b_term})'
            string += b_term
        if k < n:
            string += '+'
    print(string)
    return string


def eval_expression(expr):  # expr = str
    """Returns an evaluated expression"""
    val = eval(expr)
    print(val)
    return val


# För e

def e_deriv(a, b, x, h=0.00000001):
    """Returns the derivative of exponential functions of the form 'a*e**b*x'"""
    k = (math.e**(b*h)-1)/h
    print(k)
    return a*k*math.e**(b*x)

def get_k(base):
    """Returns the natural logarithm (ln) of base"""
    h = 0.0000001
    k = (base**h - 1)/h
    print(k)
    return k


def geo_sum(a, k, n):
    return (a*((k**n)-1))/(k-1)


def geo_sum_get_a(k, n, m):
    return (m*(k-1))/((k**n)-1)


def exponential_growth(a, k, n):
    return a*k**n


def pythagoras_sats(a, b):
    """Returns the length of the hypotenuse of a triangle with sides of lengths a and b """
    return np.sqrt(a**2 + b**2)


def deriv(f, x, prec=5):                                       # type(f) = function, prec = number of zeroes
    h = float('0.{}1'.format('0' * prec))                      # Step-size
    return (f(x+h) - f(x))/h                                   # Definition of derivative

def limit_deriv(f, x):
    h = symbols('h')
    _expr = (f(x + h) - f(x))/h
    return limit(_expr, h, 0)

def losningsmetoden(p, q):
    try:
        x1 = -p/2 - np.sqrt((p / 2) ** 2 - q)
        x2 = -p / 2 + np.sqrt((p / 2) ** 2 - q)
        print(x1, x2)
    except Exception:
        print('Got an exception')
        print(sys.exc_info())
        x1, x2 = 0, 0
        pass

    if x1 and x2:
        print(f'x1: {x1}, x2: {x2}')
        return x1, x2
    elif x1:
        print(f'x1: {x1}')
        return x1
    elif x2:
        print(f'x2: {x2}')
        return x2
    else:
        print('Inga reella lösningar')
        return


def expontentialfunktionen(c, a, x=1, prec=2):
    ap = round(a ** x, prec)
    y = round(c * ap, prec)
    s = round((ap-1)*100, prec)

    print('y = c * a**x')
    print(f'y = {c} * {a}**{x}')
    print(f'y = {c} * {ap}')
    print(f'y = {y}')
    print(f's = {s}%')
    return c * a ** x


def flatten_list(orig_list): # use recursion to make multidimensional arrays flat
    """flattens a list"""
    flat_list = []
    return next_layer(orig_list, flat_list)


def next_layer(orig_list, flat_list):
    """helper-function for flatten_list"""
    for j in orig_list:
        if type(j) == list:
            next_layer(j, flat_list)
        else:
            flat_list.append(j)
    return flat_list


def rwr(n, prec=2):
    """Round with remainder, returns the rounded number and the remainder"""
    rn = round(n, prec)
    rem = n - rn
    return rn, rem


def iterorelse(data, f, *args, **kwargs):
    """Takes an iterable or value and passes it into a function (f) elementwise.
    Returns the output of f for all values in data"""
    try:
        object_iter = iter(data)
    except TypeError:
        try:
            return f(data, *args, **kwargs)
        except TypeError as te:
            raise te
    else:
        if type(data) == dict:
            return dict([(i, f(j, *args, **kwargs)) for i, j in data.items()])
        else:
            return [f(i, *args, **kwargs) for i in data]


def convert_base(base, val):
    """
    converts from any base n to any other base

    :param base: the base to convert to
    :param val: the value that is converted
    :return: log_base(val)
    """
    return math.log(val)/math.log(base)

