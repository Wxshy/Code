def xor(a, b):
    xorResult = []
    a = list(str(a))
    b = list(str(b))
    for i in range(len(a)):
        if a[i] == b[i]: xorResult.append(0)
        else:  xorResult.append(1)
    return xorResult
