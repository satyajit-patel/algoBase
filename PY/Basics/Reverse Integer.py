class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0
        x = abs(x)
        nums = []

        while x:
            lastDigit = x % 10
            x //= 10
            nums.append(lastDigit)

        """
        120 -> int
        [0, 2, 1] -> List
        0 * 10 + 0 = 0
        0 * 10 + 2 = 2
        2 * 10 + 1 = 21
        """

        ans = 0

        for ele in nums:
            ans = ans * 10 + ele
            if ans > (2 ** 31) - 1:
                return 0

        if isNeg:
            ans *= -1
        
        return ans