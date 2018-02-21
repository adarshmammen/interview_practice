# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        p1 = l1
        p2 = l2
        carry = 0
        while p1 != None or p2 != None or carry != 0:
            add1,add2 = 0,0
            if p1 == None and p2 == None:
                add1 = 0
                add2 = 0
            elif p1 == None:
                add1 = 0
                add2 = p2.val
                p2 = p2.next
            elif p2 == None:
                add1 = p1.val
                add2 = 0
                p1 = p1.next
            else:
                add1 = p1.val
                add2 = p2.val
                p1 = p1.next
                p2 = p2.next
            temp = add1 + add2 + carry
            carry = temp/10
            res.append(temp%10)
        
        return res
        
