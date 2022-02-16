class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #https://www.youtube.com/watch?v=pzrETSYdR6Q
        min_dq = deque()
        max_dq = deque()

        start = 0
        max_len = 0

        for i in range(len(nums)):
            # start moves when max/min ele - current element exceedes the limit
###
            while min_dq and abs(nums[i] - min_dq[0][0]) > limit:
                start = min_dq.popleft()[1] + 1

            while max_dq and abs(nums[i] - max_dq[0][0]) > limit:
                # take the max of the start value because we want the narrowest valid range for new window and the start when popping off min_dq above might have been later
                # we are comparing the start we got from min_q with this one and taking the max , we want window to be as narrow as possible
                start = max(start, max_dq.popleft()[1] + 1)
###
            # insert the element into the monotonic deques.
            # inclusive comparisons (>=, <=) because we only care about
            # the latest index of the given value when narrowing the bounds.
            while min_dq and min_dq[-1][0] >= nums[i]:
                #onlypopif nums[i] <minq[0]
                min_dq.pop()
            min_dq.append([nums[i], i])

            while max_dq and max_dq[-1][0] <= nums[i]: #onlypopif nums[i] greter than maxq
                max_dq.pop()
            max_dq.append([nums[i], i])

            # calculate and compare new length of window containing element i
            max_len = max(max_len, (i - start) + 1)

        return max_len
            
