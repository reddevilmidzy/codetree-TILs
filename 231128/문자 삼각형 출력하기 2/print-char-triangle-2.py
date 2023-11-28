alp = lambda x: chr(x%26+65)
n = int(input())
m = (n+1)//2

arr = [['']*m for _ in range(n)]
cnt = 0
for j in range(m-1, -1, -1):
    for i in range(j, n-j, 1):
        arr[i][j] = alp(cnt)
        cnt += 1

for i in arr:
    print(*i)