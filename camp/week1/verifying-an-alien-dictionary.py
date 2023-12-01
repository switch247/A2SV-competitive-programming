class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m={}
        for i,v in enumerate(order):
            m[v] =i
        print(m)
        def to_int(x:str):
            t= []
            for i in x:
                t.append( m[i] )
            return t
        for i in range( 1, len(words) ):
            print( to_int(words[i-1]), to_int(words[i]) )
            if to_int(words[i]) < to_int(words[i-1]): return False
            
        return True