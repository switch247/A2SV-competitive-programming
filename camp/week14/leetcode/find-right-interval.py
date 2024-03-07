class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        vis = [ (v, i) for i,v in enumerate(intervals)]
        vis.sort()
        n =len(intervals)
        def find(target):
            low=0
            high=len(intervals)-1
            if vis[n-1][0][0]<target:
                return -1 
            while low<=high:
                mid=(low+high)//2
                if vis[mid][0][0]>=target:
                    high=mid-1
                else:
                    low=mid+1
            return vis[low][1]
        
        ans = [-1]* len(intervals)
        for num in vis:
            z = find(num[0][1])
            ans[ num[1] ]=  z
        print(ans)
        return ans