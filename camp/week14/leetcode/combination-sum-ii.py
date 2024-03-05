class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        prev = None
        def backtrack (i, path, ss):
            nonlocal prev
            # print(path)
            if ss == target:
                if path not in ans:
                    ans.append(path[:])
                return 
                        
            for j in range(i, len(candidates)):
                path.append( candidates[j] )
                if prev!= candidates[j] and ss + candidates[j]  <= target:
                    backtrack(j+1, path, ss+ candidates[j]  )
                prev = path.pop()
    
    

            return
        # 1 2 3 4 
        ans = []
        backtrack(0,[],0)
        return ans