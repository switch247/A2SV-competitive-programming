# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        rev = None
        while cur:
            tmp = cur.next
            cur.next = rev
            rev = cur
            cur = tmp
        return rev