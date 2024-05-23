class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in  word:
            x = ord(w) -97
            if not cur.children[x]:
                cur.children[x] = TrieNode()
            cur =  cur.children[x] 
            
        cur.is_end  = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        def helper(j, cur):
            n = len(word)
            for i in range(j,n):
                if word[i] !='.':
                    x = ord(word[i]) -97
                    if cur.children[x]:
                        cur = cur.children[x] 
                    else:
                        return False
                else:
                    for k in range(26):
                        if  cur.children[k] and helper(i+1, cur.children[k] ):
                            return True
                    return False
            return cur.is_end
        return helper(0,cur)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)