# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        cur = dummy
        x  = list1
        y  = list2
        while x and y:
            # print(x.val, y.val)
            if x.val <= y.val:
                cur.next = x
                cur = cur.next
                x = x.next
            else:
                cur.next = y
                cur = cur.next
                y = y.next

        if x:cur.next = x
        if y: cur.next = y
        
        return dummy.next

        