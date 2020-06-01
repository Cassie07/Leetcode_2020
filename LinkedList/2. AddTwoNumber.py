# medium
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)
        root.next = l1
        # [5], [5] if no carry here, code will stop at 0 and 1 will not be add into the linked list.
        # expected output: [0,1], wrong output: [0]
        while l1 or l2 or carry:  
            # if not v1 = v2 = 0, the last iteration will continue forever because carry will never be none.
            v1 = v2 = 0 
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val  
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)  # add node into linked list
            n = n.next # move pointer to the next one
        return root.next
