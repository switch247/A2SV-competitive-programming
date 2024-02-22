class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cpy = [-1]* n
        forward_dict = {}
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                forward_dict[stack.pop()] = i
            stack.append(i)
        
        for i in range(n):
            if i not in forward_dict:
                for j in range(i):
                    if nums[j] > nums[i]:
                        cpy[i] = nums[j]
                        break
            else:
                cpy[i] = nums[forward_dict[i]]
        return cpy