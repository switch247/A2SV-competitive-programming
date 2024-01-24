# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode(None)
        even_head = even
        odd = ListNode(None)
        odd_head = odd
        cur = head
        i = 1
        while cur:
            if i%2:
                odd.next = cur
                odd = odd.next
            else:
                even.next  = cur
                even = even.next
            cur = cur.next
            i+=1
        # print(even_head, odd_head)
        odd.next = even_head.next
        even.next = None
        return odd_head.next