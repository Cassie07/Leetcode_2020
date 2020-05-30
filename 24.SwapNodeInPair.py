class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
#         step = 0
#         root = cur = ListNode(0)
#         root.next = head
#         slow = head
#         while slow:
#             step += 1
#             if step % 2 == 1:
#                 continue
#             else:
#                 fast = slow.next
#                 if fast == None:
#                     return root.next
#                 slow.next = fast.next
#                 fast.next = slow
#                 cur.next = fast
#                 cur = slow
#                 slow = slow.next
#         return root.next
        step = 0
        root = ListNode(0)
        root.next = head
        cur = root
        slow = head
        while slow and slow.next:
            step += 1
            if step%2 == 1:
                continue
            else:
                fast = slow.next
                slow.next = fast.next
                fast.next = slow
                cur.next = fast
                cur = slow
                slow = slow.next
        return root.next
