mp = {}
n = int(input())
for _ in range(n):
    nums = input().split()
    name = nums[0]
    vals = list(map(float, nums[1:]))
    mp[name] = vals
name = input()

ans = sum(mp[name])/len(mp[name])
print(f"{ans:.2f}")