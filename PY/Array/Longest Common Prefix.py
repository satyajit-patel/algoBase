class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = 10**8
        
        for it in strs:
            minLen = min(minLen, len(it))
        
        ans = ""
        
        for i in range(minLen):
            flag = True
            ch = strs[0][i]
            
            for it in strs:
                if(it[i] != ch):
                    flag = False
                    break
                    
            if(not flag):
                break
            
            ans += ch
        
        return ans
    
    """
    https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
    """