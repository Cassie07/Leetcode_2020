# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        head2 = self.FindMid(head)
        head2 = self.reverse(head2)
        while head and head2:
            if head.val != head2.val:
                return False
            else:
                head = head.next
                head2 = head2.next
        return True
            
    def FindMid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self,head):
        slow = None
        fast = head
        while fast:
            tmp = fast.next
            fast.next = slow
            slow = fast
            head = fast
            fast = tmp
        return head
