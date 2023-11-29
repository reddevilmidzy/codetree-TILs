def rec(num):
    if num <= 2:
        return num
    return rec(num-2) + num
n = int(input())
print(rec(100 - n%2) - rec(n-2))