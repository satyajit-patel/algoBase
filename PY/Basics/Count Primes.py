class Solution:
    primes = [1] * ((10**6) * 5 + 2)

    def init(self):
        self.primes[0] = 0
        self.primes[1] = 0

        for i in range(2, len(self.primes)):
            if self.primes[i]:
                for j in range(i * 2, len(self.primes), i):
                    self.primes[j] = 0

    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        """
        0 <= n <= 10**6
        so O(n * logn) or O(n * sqrt(n)) will work
        """
        ans = 0

        # TLE
        # for i in range(2, n): # O(n)
        #     if self.isPrime(i): # O(sqrt(n))
        #         ans += 1

        if self.primes[0]:
            self.init() # O(n * logn) one time
        
        # print(self.primes)

        for i in range(2, n): # O(n)
            if(self.primes[i]):
                ans += 1

        return ans