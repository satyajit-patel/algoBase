class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        totEle = n * m
        ans = []
        istCol, lastCol, istRow, lastRow = 0, m-1, 0, n-1
        
        while(len(ans) < totEle):
            for i in range(istCol, lastCol+1):
                ans.append(matrix[istRow][i])
            istRow += 1
            
            for i in range(istRow, lastRow+1):
                ans.append(matrix[i][lastCol])
            lastCol -= 1

            """
            https://leetcode.com/problems/spiral-matrix/submissions/1869350332/?source=submission-noac
            """
            if len(ans) >= totEle:
                break
            
            for i in range(lastCol, istCol-1, -1):
                ans.append(matrix[lastRow][i])
            lastRow -= 1
            
            for i in range(lastRow, istRow-1, -1):
                ans.append(matrix[i][istCol])
            istCol += 1
        
        return ans