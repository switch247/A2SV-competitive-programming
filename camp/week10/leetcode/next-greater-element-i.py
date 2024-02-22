class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dic={}
        for i in nums2:
            while stack and  stack[-1]< i:#if stack is not empty
                k=stack.pop()
                dic[k]= i
            stack.append(i)
        #print(d)
        for i in range (len(nums1)):
            if nums1[i] in dic:
                nums1[i] = dic[nums1[i]]
            else:
                nums1[i]=-1
        return nums1