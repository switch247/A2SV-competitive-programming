class Solution:
    def minimumPushes(self, word: str) -> int:
        alpha = [0] * 26
        for ch in word:
            alpha[ord(ch) - ord('a')] += 1
        
        # Sort counts in descending order
        sorted_counts = sorted(alpha, reverse=True)
        
        ans = 0
        for index, count in enumerate(sorted_counts):
            if count == 0:
                return ans 
            ans += ((index // 8 )+ 1) * count
        
        return ans    