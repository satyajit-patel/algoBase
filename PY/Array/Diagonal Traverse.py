from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(m):
                k = i + j # trick https://www.youtube.com/watch?v=7HAKiGZSrWc
                d[k].append(mat[i][j])
        
        ans = []
        up = True
        
        for i in range(len(d)):
            l = d[i]
            if up:
                l.reverse()
                ans.extend(d[i])
            else:
                ans.extend(l)
            up = not up
        
        return ans
    """
    https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
    """