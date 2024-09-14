class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        invalid  =0
        allowed_chars = set(i for i in allowed)
        for word in words:
            for c in word:
                if c not in allowed_chars:
                    invalid+=1
                    break
        return len(words) - invalid
        
