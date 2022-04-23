def dbs(keys, values):
    """
    Will return a zip of (keys, values) where values are sorted in descending order.
    Related keys are switched as well.
    """

    for passnum in range(len(keys) - 1, 0, -1):
        for i in range(passnum):
            if values[i] > values[i + 1]:
                temp_r = values[i]
                temp_n = keys[i]

                values[i] = values[i + 1]
                keys[i] = keys[i + 1]

                values[i + 1] = temp_r
                keys[i + 1] = temp_n

    return tuple(zip(keys, values))
