from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
words = [''.join(sorted(input().rstrip())) for _ in range(n)]
fore = []
back = []
for word in words:
    fore.append(word)
    back.append(word[::-1])

fore.sort()
back.sort()

for word in words:
    # l = bisect_left(fore, word[::-1])
    # r = bisect_right(fore, word[::-1])
    # print("l",l,"r",r)
    print(bisect_left(back, word)+1, bisect_right(fore, word[::-1]))
# print(fore)
# print(back)