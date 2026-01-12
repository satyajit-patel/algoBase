class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        # print(nums)

        import itertools
        ans = []
        for p in itertools.permutations(nums):
            # print(f"{p} - {type(p)}")
            ans.append("".join(map(str, p)))

        return ans[(k-1) % len(ans)]