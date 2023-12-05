class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # qwertyuiop
        # asdfghjkl
        # zxcvbnm
        answer = []
        flag = False
        for word in words:
            rows = set()
            for ch in word.lower():
                if ch  in "qwertyuiop": rows.add("1")
                elif ch  in "asdfghjkl": rows.add("2")
                elif ch  in  "zxcvbnm" :rows.add("3")
                else:
                    continue
            if len(rows)==1: answer.append(word)
            rows.clear()
        return answer
            


        