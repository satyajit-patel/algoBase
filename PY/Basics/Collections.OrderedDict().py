# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
from collections import defaultdict
netPrice = defaultdict(int) # dict - ordered, set - unordered
for _ in range(int(input())):
    *name, price = input().split()
    name = " ".join(name)
    price = int(price)
    netPrice[name] += price

for k, v in netPrice.items():
    print(k, v)
