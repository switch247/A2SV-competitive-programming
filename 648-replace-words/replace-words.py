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

    def search(self, word: str) -> bool:
        cur = self.root
        ww = ''
        for w in  word:
            x = ord(w) -97
            if cur.children[x]:
                ww+=w
                if cur.children[x].is_end:
                    return ww
                cur =  cur.children[x] 
                
            else:
                return word
        return ww
        # cur.is_end

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()
        for w in dictionary:
            t.insert(w)
        
        # print(t)
        ans = []
        for w in sentence.split(' '):
            ans.append(t.search(w))

        return ' '.join(ans)