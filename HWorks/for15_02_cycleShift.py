a = [1, 2, 3, 4, 5]
b = int(input())

# my simple sample
def shift(a, b):
    """
    should do cycle (left/right, depends on sigh of number) shift for array a in the specified dir
    :param a: array
    :return: array 'an' with left cycle shift
    """


    an = [] # a = [1, 2, 3, 4, 5]

    # right shift
    if b >= 0:
        for i in range(abs(b)):
            an.append(a[len(a) + i - b])

        for i in range(len(a) - b):
            an.append(a[i])

    # left shift
    else:
        tmp = []
        for i in range(b, 0):
            tmp.append(a[len(tmp)])

        an = a[abs(b)::] + tmp

    return an


# good sample
def goodShift(a, b):
    if b > 0:
        for i in range(b):
            a.insert(0, a.pop())

    else:
        for i in range(abs(b)):
            a.append(a.pop(0))

    return a


print(shift(a, b), goodShift(a, b))
