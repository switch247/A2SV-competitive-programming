# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        cur = head.next
        prev = head
        prev.next = None
        while cur:
            prev_copy = prev
            temp = prev_copy
            flag = False
            while prev_copy and cur.val < prev_copy.val:
                temp = prev_copy
                prev_copy = prev_copy.next
                flag = True
            if flag:
                cur_next = cur.next
                temp.next = cur
                cur.next = prev_copy 
                cur = cur_next
            else:
                cur_next = cur.next

                cur.next = prev 
                prev = cur

                cur = cur_next
        
        # print(prev)
        rev = None
        cur = prev
        while cur:
            tmp = cur.next
            cur.next = rev 
            rev = cur
            cur = tmp
        return rev



            


        