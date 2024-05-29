class Trie:
    def __init__(self):
        self.count = 1
        self.children = [ None for _ in range(26) ]
    
    def insert(self, word: str) -> None:
        c = 0
        cur = self
        for w in  word:
            x = ord(w) -97
            if cur.children[x]:
                cur.children[x].count+=1
            else:
                cur.children[x] = Trie()
            c += cur.children[x].count
            cur =  cur.children[x]  
        return c  

    def search(self, word: str) -> bool:
        cur = self
        c = 0
        
        for i,w in  enumerate(word):
            x = ord(w) -97
            if cur.children[x].count == 1:
                return c + ((len(word) - i) if cur else 0)
            c +=cur.children[x].count
            cur =  cur.children[x] 
        return c

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n = len(words)
        # d = { words[i]:i for i in range(n)}
        # words.sort()
        # print(words, d)
        ans = [0]*n

        t = Trie()
        for w in words: 
            x = t.insert(w)
            # ans[d[w]] = x
        for i in range(n):
            ans[i] = t.search(words[i])
        return ans
        

    