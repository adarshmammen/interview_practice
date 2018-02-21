# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        p = None
        head = None
        while l1 or l2:
            if not l1:
                val = l2.val
                l2 = l2.next
            elif not l2:
                val = l1.val
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    val = l2.val
                    l2 = l2.next
                else:
                    val = l1.val
                    l1 = l1.next
            
            if not p:
                p = ListNode(val)
                head = p
            else:
                p.next = ListNode(val)
                p = p.next
        return head
