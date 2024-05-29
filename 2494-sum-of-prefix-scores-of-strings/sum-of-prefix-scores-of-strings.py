class Trie:
    def __init__(self):
        self.count = 1
        self.children = [ None for _ in range(26) ]
    
    def insert(self, word: str) -> None:
        cur = self
        for w in  word:
            x = ord(w) -97
            if cur.children[x]:
                cur.children[x].count+=1
            else:
                cur.children[x] = Trie()
            cur =  cur.children[x]    

    def search(self, word: str) -> bool:
        cur = self
        c = 0
        for w in  word:
            x = ord(w) -97
            c +=cur.children[x].count
            cur =  cur.children[x] 

        return c

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = Trie()
        for w in words:
            t.insert(w)
        n = len(words)
        ans = [0]*n
        for i in range(n):
            ans[i] = t.search(words[i])
        return ans
        

    