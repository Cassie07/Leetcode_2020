class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val or l1.val == l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return root.next
    
    # # in-place, iteratively        
    # def mergeTwoLists(self, l1, l2):
    #     if None in (l1, l2):
    #         return l1 or l2
    #     dummy = cur = ListNode(0)
    #     dummy.next = l1
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             l1 = l1.next
    #         else:
    #             nxt = cur.next
    #             cur.next = l2
    #             tmp = l2.next
    #             l2.next = nxt
    #             l2 = tmp
    #         cur = cur.next
    #     cur.next = l1 or l2
    #     return dummy.next
    
    
