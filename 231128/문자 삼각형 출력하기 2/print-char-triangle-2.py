n = int(input())
m = (n+1)//2

arr = [['']*m for _ in range(n)]

for j in range(m-1, -1, -1):
    print("j",j)
    for i in range(m-j, n, 1):
        print(i,j)