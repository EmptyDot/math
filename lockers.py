"""
A puzzle from https://twitter.com/3blue1brown/status/1522749517422112772

A hallway has lockers numbered 1,...,N, all initially closed.
Student 1 opens all of them.
Student 2 closes lockers 2, 4, 6, 8, etc.
Student 3 toggles every third locker, meaning if it’s closed, they open it, if it’s open, they close it.
Student 4 toggles every fourth locker.
Etc., with the k'th student toggling every k’th locker.
After N students do this, which lockers are open, and which are closed?
"""

import numpy as np

def main(n):
    """
    :param n: integer: side length of a square. N = n**2
    """
    lockers = list(np.zeros(n**2, dtype=int))

    for i in range(1, n**2 + 1):
        for j in range(i - 1, n**2, i):
            locker = lockers[j]
            if locker:
                lockers[j] = 0
            else:
                lockers[j] = 1

    arr = np.array(lockers).reshape((n, n))
    opened = []
    for y, row in enumerate(arr):
        for x in np.where(row == 1)[0]:
            opened.append(n * y + x + 1)
    print(opened)


if __name__ == '__main__':
    main(10)
