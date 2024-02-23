class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        ans=[]
        for r in range(len(nums)):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            # print(q)
            if r-l+1 ==k:
                # print(nums[l:r+1])
                # print(r-l+1)
                ans.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l+=1 
        return ans

        