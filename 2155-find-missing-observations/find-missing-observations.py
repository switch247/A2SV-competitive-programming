class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        cur = sum(rolls) 
        m = len(rolls)
        target = (n+m)*mean  - cur
        print(target)
        if target>6*n or target<n:
            return []
        q , r = divmod(target, n)
        return [q+1]*r + [q]*(n-r)
        