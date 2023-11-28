def mul(n,m):
    if m == 1:
        return n
    elif m == 0:
        return 1
    
    return mul(n, m-1) * n

a,b = map(int,input().split())

x = mul(a,b)
y = mul(b,a)

if y < x:
    x,y = y,x

print(y-x)