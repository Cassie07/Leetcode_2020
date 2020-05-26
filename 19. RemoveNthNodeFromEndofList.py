# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # must have this code or [1](n = 1) will fail
        # preparing for removing the only node in the linkded list
        mem = true_root = ListNode(0)
        mem.next = head
        root = head
        length = 0 
        # calculate length of the linked list
        while root:
            length += 1
            root = root.next
        stop = length - n
        # mem to the node before the removed node
        for i in range(stop):
            mem = head
            # head to the node after the removed node
            head = head.next
        # remove
        mem.next = head.next
        return true_root.next
