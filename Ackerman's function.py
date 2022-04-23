def ack(m, n):
    if m == 0:
        ans = n + 1
    elif n == 0:
        ans = ack(m - 1, 1)
    else:
        ans = ack(m - 1, ack(m, n - 1))
    return ans


try:
    for i in range(6):
        for j in range(6):
            print(f'Ackerman {(i, j)} is: {ack(i, j)}')
except RecursionError as Ex:
    print(Ex)
    pass
