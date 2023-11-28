alp = lambda x: chr(x%26 + 65)
n = int(input())
arr = [['']*n for _ in range(n)]
idx = 0

for j in range(n-1, -1, -1):
    for i in range(n-1, -1, -1):
        arr[i][j] = alp(idx)
        idx += 1

for res in arr:
    print(*res)