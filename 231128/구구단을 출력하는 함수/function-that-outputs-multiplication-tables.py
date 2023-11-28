a,b,c = sorted(list(map(int,input().split())))
for i in range(a, c+1):
    if i == b: continue
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")