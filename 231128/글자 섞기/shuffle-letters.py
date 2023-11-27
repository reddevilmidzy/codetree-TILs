from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
words = []
fore = []
back = []

for i in range(n):
    s = input().rstrip()
    ss = "".join(sorted(s))
    words.append(ss)
    # fore.append((ss, i))
    # back.append((ss[::-1], i))
    fore.append(ss)
    back.append(ss[::-1])
fore.sort(key=lambda x:x[0])
back.sort(key=lambda x:x[0])


for word in words:
    print(bisect_left(back, word)+1,end=' ')
    val = bisect_left(fore, word[::-1])
    print(val + (val == 0))