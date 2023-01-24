# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_int(node):
            if node:
                return node.val + 10 * to_int(node.next)
            else: return 0
        
        a = to_int(l1) + to_int(l2)
        print(a)
        
        node  = ListNode(a % 10)
        curent= node
        while a > 9:
            a //= 10
            curent.next  = ListNode(a % 10)
            curent = curent.next

        return node
        
        
