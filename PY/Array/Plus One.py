class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # n = int("".join(map(str, digits)))
        # n += 1
        # return list(map(int, str(n)))
        
        """or"""
        
        # list to int
        n = 0
        for ele in digits:
            n = n * 10 + ele
            
        n += 1
        
        # int to list
        l = []
        while n:
            lastDigit = n % 10
            n //= 10
            # print(f"{lastDigit} - {n}")
            l.append(lastDigit)
            
        l.reverse()
        return l
    
    # https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/