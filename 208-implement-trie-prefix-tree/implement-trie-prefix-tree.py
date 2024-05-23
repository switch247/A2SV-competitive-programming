class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in  word:
            x = ord(w) -97
            if cur.children[x]:
                cur =  cur.children[x] 
            else:
                cur.children[x] = TrieNode()
                cur =  cur.children[x] 
            
        cur.is_end  =True
        # https://leetcode.com/playground/jx6mSTWN

    def search(self, word: str) -> bool:
        cur = self.root
        for w in  word:
            x = ord(w) -97
            if cur.children[x]:
                cur =  cur.children[x] 
            else:
                return False
        return cur.is_end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        n = len(prefix)
        for i in range(n):
            x = ord(prefix[i]) -97
            if cur.children[x]:
                cur = cur.children[x] 
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)