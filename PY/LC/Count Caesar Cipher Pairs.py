from collections import Counter

class Solution:
    def countPairs(self, words):
        freq = Counter()
        for w in words:
            sig = tuple((ord(c) - ord(w[0])) % 26 for c in w)
            freq[sig] += 1
        ans = 0
        for v in freq.values():
            ans += v * (v - 1) // 2
        return ans

"""
Suppose words = ["ab", "bc", "za"]

Step 1:
For each word, create a "signature"—the difference from the first letter, mod 26.

"ab": (0, 1)
"bc": (0, 1)
"za": (0, 1)
So all have the same signature.

Step 2:
Count how many words share the same signature. Here, freq = {(0, 1): 3}

Step 3:
For each group, count pairs: n(n−1)/2
"""©leetcode