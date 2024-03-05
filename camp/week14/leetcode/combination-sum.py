class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack (i, path):
            # print(path)
            ss = sum(path)
            if ss == target:
                if sorted(path) not in ans:
                    ans.append(path[:])
                return False
            elif ss > target:
                return True
                        
            if i <len(candidates):
                
                
                path.append( candidates[i] )
                backtrack(i+1, path)

                # repeat
                if  not backtrack(i+1, path+[candidates[i]]):
                    backtrack(i, path+[candidates[i]] )
                
                # do not choose
                path.pop()
                backtrack(i+1, path)

            return
        # 1 2 3 4 
        ans = []
        backtrack(0,[])
        return ans
        