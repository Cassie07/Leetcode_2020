class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        # 1. has cycle?
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else: # fast.next.next/ fast.next == None
            return None
                  
        # 2. find the start(end) of the circle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
