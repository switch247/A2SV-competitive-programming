# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dic = {}
        cur = head
        count = 0
        while cur:
            dic[count] = cur
            cur = cur.next
            count +=1
        target = len(dic) - n
        if len(dic) == 1: return None # only 1 element

        if target == 0: head = dic[target].next #first element
        elif n ==1: dic[target-1].next = None  #last element
        else: dic[target-1].next = dic[target+1]
        return head
        
