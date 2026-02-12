class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freq= defaultdict(int)
            for j in range(i, len(s)):
                freq[s[j]]+=1
                if len(set(freq.values())) == 1:
                     ans = max(ans, j-i+1)
        return ans