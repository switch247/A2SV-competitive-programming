# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        s= []
        while(temp):
            s.append(str( temp.val ))
            temp = temp.next
        
        return s==s[::-1]




# better aproach reverse half of the linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None: return True
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse half
        # 123 321 -> 123 123
        # print(slow)
        # print(head)

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # print(head, slow)
        # print(prev)
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
