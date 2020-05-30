# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # mine
        root = ListNode(0)
        root.next = head
        cur = root
        step = 0
        while cur and cur.next:
            head = cur.next
            # step != 0 : avoid the value of the first node is 0(the value of cur is 0)
            if cur.val == head.val and step != 0:
                cur.next = head.next
            else:
                cur = cur.next
            step += 1
        return root.next
        
        # A better one
        slow, fast = head, head.next if head else None
        while fast:
            if slow.val == fast.val:
                fast = fast.next
                slow.next = fast
            else:
                slow = fast
                fast = fast.next
        return head
