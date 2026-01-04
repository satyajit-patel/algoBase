class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mat = []
        
        for i in range(numRows):
            l = [1] * (i+1)
            for j in range(1, i):
                l[j] = mat[i-1][j] + mat[i-1][j-1]
            mat.append(l)
        
        return mat
    
    """
    https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/
    """