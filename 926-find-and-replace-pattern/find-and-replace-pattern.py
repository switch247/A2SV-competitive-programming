class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        for word in words:
            is_valid = True
            d: dict[str, str] = {}
            ls: list[int] = [0] * 26
            size = len(word)
            for i in range(size):
                if d.get(pattern[i]):
                    if d.get(pattern[i]) != word[i]:
                        is_valid = False
                        break
                else:
                    if ls[ord(word[i]) - 97] != 0:
                        is_valid = False
                        break
                    else:
                        d[pattern[i]] = word[i]
                        ls[ord(word[i]) - 97] += 1
            if is_valid:
                answer.append(word)
        return answer
