class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack (first_num, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            for num in range(first_num,n+1):
                path.append(num)

                backtrack(num+1, path)
                
                path.pop()
            return
        # loop num ==1 # 1,[], 
        #   2,[1] =>[1,2](len==2)
        #   3 ret , pop()
        #   3,[1] => [1,3]
        #   4 ret pop
        #   4, [1],pop
        # loop num ==2 # 2, []=> [2]
        #   3, [2]=> [2,3]
        # X for num in range (3, 3) n =2
        ans = []
        backtrack(1,[])
        return ans