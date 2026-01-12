class Solution:

    primes = [2, 3, 5]

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for ele in self.primes:
            while(n % ele == 0):
                n //= ele
            if n == 1:
                return True
        
        return False