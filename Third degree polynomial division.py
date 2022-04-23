
def divide_by_x_plus_m(i, j, k, l, m, x=None):
    first_term = i
    second_term = j - m*i
    third_term = k - j*m + i*m**2
    remainder = l - k*m + j*m**2 - i*m**3

    print(first_term, second_term, third_term, remainder)
    expr_str = ''
    if first_term != 0:
        if first_term == 1 or first_term == -1:
            if first_term == -1:
                expr_str += '-'
            expr_str += 'x**2'
        else:
            expr_str += f'{first_term}x**2'

    if second_term != 0:
        if second_term > 0:
            expr_str += '+'
        if second_term == 1 or second_term == -1:
            if second_term == -1:
                expr_str += '-'
            expr_str += 'x'
        else:
            expr_str += f'{second_term}x'

    if third_term != 0:
        if third_term > 0:
            expr_str += '+'
        expr_str += f'{third_term}'

    if remainder != 0:
        if remainder > 0:
            expr_str += '+'
        expr_str += f'{remainder}/(x + {m})'

    if x:
        f = i * x ** 2 + (j * x - m * i * x) + (k - j * m + i * m ** 2) + ((l - k * m + j * m ** 2 - m ** 3) / (x + m))
        print(expr_str + ' = ' + f)
    else:
        print(expr_str)
    return





def all_x_plus_m(coefficients, y, x=None):
    ans_str = ''
    n = len(coefficients) - 1
    for m in range(1, len(coefficients) + 1):
        coeff = mth_term(coefficients, m, y, x)
        term = ''
        exp = n - m

        if coeff != 0:

            if coeff == -1:
                ans_str += '-'

            elif coeff > 0 and m != 1:
                ans_str += '+' + str(coeff)

            elif coeff == 1:
                pass
            elif coeff == -1:
                pass
            else:
                term += str(coeff)
        print(coeff, m, exp)
        if exp != 0:
            if exp == 1:
                term += 'x'
            elif exp == -1:
                if y < 0:
                    term += f'/(x{y})'
                elif y == 0:
                    term += f'/x'
                else:
                    term += f'/(x+{y})'
            else:
                if coeff != 0:
                    term += f'x**{exp}'

        ans_str += f'{term}'

    orig_expr = ''
    divisor = 'x'
    orig_exp = n
    for c in coefficients:
        orig_expr += f'{c}x**{orig_exp}'
        orig_exp -= 1
        if c < 0:
            orig_expr += '+'
    if y >= 0:
        divisor += '+' + str(y)
    else:
        divisor += str(y)

    orig_expr = f'({orig_expr})/{divisor}'
    print(f'{orig_expr=}')
    return ans_str


def mth_term(coefficients, m, y, x=None):
    n = len(coefficients) - 1
    a = coefficients

    ans = 0
    for i in range(m):
        if x:
            term = a[m-i]*y**i*x**(n-m)
        else:
            term = a[m-i-1]*y**i

        if i % 2 == 0:
            ans += term
        else:
            ans -= term

    return ans


if __name__ == '__main__':
    print(all_x_plus_m([-2, 6, 2, -4], 2))

