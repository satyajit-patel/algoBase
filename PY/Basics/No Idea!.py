n, m = map(int, input().split())
nums = list(map(int, input().split()))
st1 = set(map(int, input().split()))
st2 = set(input().split())
st2 = set([int(ele) for ele in st2])

# print(st1)
# print(st2)

happiness = 0

# # O(n * n) - TLE
# for ele in nums:
#     if ele in st1:
#         happiness += 1
#     if ele in st2:
#         happiness -= 1

# O(nlogn)
l1 = sorted(list(st1))
l2 = sorted(list(st2))

# print(l1)
# print(l2)

import bisect as bs

# O(n * logn)
for ele in nums:
    lb1 = bs.bisect_left(l1, ele)
    if (lb1 != m) and (ele == l1[lb1]):
        happiness += 1
        
    lb2 = bs.bisect_left(l2, ele)
    if (lb2 != m) and (ele == l2[lb2]):
        happiness -= 1
    # print(lb1, lb2, ele)

print(happiness)

# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

