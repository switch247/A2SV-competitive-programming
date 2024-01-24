# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #head = [4,5,1,9], node = 5 
        # [4,1,1,9]
        #the nodes value becomes value of the next(next element is guarenteed)
        #the node next to the node is skiped
        node.val = node.next.val
        node.next = node.next.next
        