class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        # if len(word)==1:
        #     x = ord(word) -97
        #     cur.children[x] = TrieNode()
        #     return
        for w in  word:
            x = ord(w) -97
            if cur.children[x]:
                cur =  cur.children[x] 
            else:
                cur.children[x] = TrieNode()
                cur =  cur.children[x]
        cur.is_end  =True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        n = len(words)
        t = Trie()
        cur = t.root
        for w in words:t.insert(w)
        
        pos = [(t.root,[])]

        ret = ''
        while pos:
            curr, path = pos.pop()
            if len(ret)<=len(path):
                ret =  path
            for i, neig in enumerate(curr.children):
                if neig and neig.is_end:
                    nxt = path[:] + [chr(i+97 )]
                    pos.append((neig,nxt))
        return ''.join(ret)




