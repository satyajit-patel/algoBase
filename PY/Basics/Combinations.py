class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        for c in itertools.combinations(list(range(1, n+1)), k):
            ans.append(list(c))
        return ans