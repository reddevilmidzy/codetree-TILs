input()
a = list(map(int,input().split()))
a.extend(list(map(int,input().split())))
print(*sorted(a))