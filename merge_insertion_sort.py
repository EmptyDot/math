import random


global odd


def split(data: list):
    groups = []
    for i in range(1, len(data), 2):
        j = i - 1

        if len(data) % 2 == 1:
            global odd
            odd = data.pop()
        else:
            group = compare(data[i], data[j])
            groups.append(group)
    return groups


def compare(a, b):
    """Helper func for split"""

    if a > b:
        return b, a
    else:
        return a, b


def sort_groups(groups):
    for i in range(1, len(groups)):

        temp = groups[i]

        j = i - 1
        while j >= 0 and temp[-1] < groups[j][-1]:

            groups[j + 1] = groups[j]
            j -= 1
        groups[j + 1] = temp
    return groups


def merge(groups):

    S = [j for i, j in groups]

    try:
        groups.append((odd, False))
    except NameError:
        pass

    S.insert(0, groups.pop(0)[0])
    idxs = order(len(groups))

    for idx in idxs:
        pair = groups[idx]
        if pair[-1]:
            pos = binary_search(S, pair[0], 0, S.index(pair[-1])) + 1
            S.insert(pos, pair[0])
        else:
            pos = binary_search(S, pair[0], 0, S.index(S[-1])) + 1
            S.insert(pos, pair[0])

    return S


def order(length):
    n = 1
    start = 0
    size = 0
    lst = list(range(length))
    while True:
        start += size
        size = 2**n - size
        stop = start + size

        temp = lst[start:stop]
        temp.reverse()
        lst[start:stop] = temp

        if stop > len(lst):
            break

        n += 1
    return lst


def binary_search(arr, key, start, end):
    # key
    if end - start <= 1:

        if key < arr[start]:
            return start - 1
        else:
            return start

    mid = (start + end)//2

    if arr[mid] < key:
        return binary_search(arr, key, mid, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid)
    else:
        return mid


"""
split -> sort_groups -> merge
"""


def main(data: list):
    return merge(sort_groups(split(data)))


d = list(range(10000))
random.shuffle(d)

main(d)




