class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        @cache
        def f(n, k):
            # base case
            if n == k:
                return 1
            if n == 0 or k == 0:
                return 0

            # recursive case
            ans = 0
            # case1 put largest stick to the end
            ans += f(n-1, k-1) 
            # case2 put non-largest stick to the end
            ans += f(n-1, k) * (n-1) 
            return ans % (10**9 + 7)
        
        return f(n, k)