class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        
        p = dummy
        
        while p and p.next:
            q = p.next
            duplicate = False
            while q and q.next and q.val == q.next.val:
                q = q.next
                duplicate = True
            if duplicate:
                p.next = q.next
            else:
                p = p.next
        
        return dummy.next
 
