n = int(input())
shoes = list(map(int, input().split()))
m = int(input())

ans = 0
from collections import defaultdict
d = defaultdict(int)
for k in shoes:
    d[k] += 1

while(m):
    size, price = map(int, input().split())
    m -= 1
    if(size in d):
        ans += price
        d[size] -= 1
        if(d[size] == 0):
            del d[size]

print(ans)

# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true