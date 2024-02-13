# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy  = ListNode(None, head)
        cur = dummy
        total = -1
        while cur:
            total+=1
            cur = cur.next
        # print(total)
        idx = 0
        cur = dummy
        while cur and cur.next:
            # print(total - idx)
            if total - idx  == n:
                cur.next = cur.next.next
            idx+=1
            cur = cur.next

        return dummy.next
        