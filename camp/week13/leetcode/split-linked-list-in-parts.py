# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, root, k):
        curr, length = root, 0
        while curr: curr, length = curr.next, length + 1
       
        # Determine the len of each chunk and Split up the list
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks  + [chunk_size] * (k - longer_chunks)
        # print(res)
        # res contains starting nodes
        prev, curr = None, root
        for index, num in enumerate(res):
            if prev:
                # cut the curent node off
                prev.next = None
            res[index] = curr
            for i in range(num):
                prev, curr = curr, curr.next
        return res