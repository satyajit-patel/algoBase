from functools import cache
class Solution:
    @cache # cache only hashes the immutable(like sts, int, tuple)
    def f(self, nums: tuple(int), i: int) -> int:
        # base case
        if(i >= len(nums)):
            return 0

        # recursive case
        take = nums[i] + self.f(nums, i+2)
        skip = self.f(nums, i+1)

        return max(take, skip)

    def rob(self, nums: List[int]) -> int:
        return self.f(tuple(nums), 0)


"""
from functools import cache

class Solution:
    nums = []

    @cache
    def f(self, i):
        # base case
        if(i >= len(self.nums)):
            return 0

        # recursive case
        take = self.nums[i] + self.f(i+2)
        skip = self.f(i+1)

        return max(take, skip)

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return self.f(0)
"""