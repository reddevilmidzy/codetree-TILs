import sys
input = sys.stdin.readline

n = int(input())
fore = []
back = []

for i in range(n):
    s = input().rstrip()

    ss = "".join(sorted(s))
    fore.append((ss, i))
    back.append((ss[::-1], i))

fore.sort(key=lambda x:x[0])
back.sort(key=lambda x:x[0])

res = [[0,0] for _ in range(n)]

for i in range(n):
    res[fore[i][1]][0] = i+1
    res[back[i][1]][1] = i+1

# print(fore)
# print(back)

for i,j in res:
    print(min(i,j), max(i,j))