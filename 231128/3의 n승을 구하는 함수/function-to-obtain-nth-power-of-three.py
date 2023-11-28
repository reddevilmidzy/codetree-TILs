def mul(n,m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    return mul(n, m-1) * n
print(mul(3, int(input())))