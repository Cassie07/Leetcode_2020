class Solution:

    # iteratively
    # def reverseList(self, head: ListNode) -> ListNode:
    #     prev = None
    #     cur = head
    #     while cur:
    #         tmp = cur.next
    #         cur.next = prev
    #         prev = cur
    #         head = cur
    #         cur = tmp
    #     return head
    
    # Recursively
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head)
    
    def reverse(self, cur, prev = None):
        if cur == None:
            return prev
        tmp = cur.next
        cur.next = prev
        return self.reverse(tmp, cur)
