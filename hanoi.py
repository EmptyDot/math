

def move(f, t):
    print(f'Move disc from {f} to {t}')


def hanoi(n, f, h, t):
    if n == 0:
        pass
    else:
        hanoi(n - 1, f, t, h)
        move(f, t)
        hanoi(n - 1, h, f, t)

hanoi(4, "A", "B", "C")
