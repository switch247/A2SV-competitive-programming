class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dic={}
        for i in nums2:
            while stack and  stack[-1]< i:#if stack is not empty(while stack: meaniing)
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

'''from collections import deque
nums1=[4,1,2]
nums2=[1,3,4,2]
stack= deque()
# or just stack=[]
d={}
for i in nums2:
    while stack and  stack[-1]< i:#if stack is not empty
        k=stack.pop()
        d[k]= i
    stack.append(i)
print(d)
for i in range (len(nums1)):
    if i in d:
        nums1[i]=d[nums1[i]]
    else:
        nums1[i]=-1
print(nums1)
#for loop :add 1 to stack b/c empty
#compare 1 and next element(i) if i>1 it is next greater element(i)
#pop 1from stack add it to dictionary and its value becomes i(3),then add i(3) to stack for next if
#iterate through nums1 if it is in dict change it to dict value else change it to -1'''
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if nums1[i]==nums2[-1]:
                        ls.append(-1)
                        break
                    else:
                        for k in range(j+1,len(nums2)):
                            if nums2[k]>nums2[j]:
                                ls.append(nums2[k])
                                break
                        #if the loop fails 
                        if max(nums2[j:])==nums2[j]:
                            ls.append(-1)
                                
                
                    
                                
        return ls
'''
