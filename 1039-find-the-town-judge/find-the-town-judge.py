class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1: return 1 #if there is only one person they are the judge
        left=set()
        right=set()
        count={}
        for i in range( len(trust) ):
            if trust[i][1] not in count: count [ trust[i][1] ]=1
            else: count[ trust[i][1] ] +=1
            left.add(trust[i][0])
            right.add(trust[i][1])
        for i in right: #he is trusted but doesnt trust
            if i not in left:
                if count[i] == n-1: #if everyone trusts i
                    return i 
                else: continue
        return -1
            
            