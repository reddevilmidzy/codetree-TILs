n = int(input())
arr = list(map(int,input().split()))

val = [0]*11

for num in arr:
    val[num//10] += 1

for i in range(10, 0, -1):
    if val[i]:
        print(f"{i*10} - {val[i]}")