# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head
        carry = 0

        while l1 or l2 or carry:    
            res = carry
            if l1:
                res += l1.val
                l1 = l1.next
            
            if l2:
                res += l2.val
                l2 = l2.next
            
            carry,val = divmod(res,10)
            current.next = ListNode(val)
            current = current.next
        
        return head.next 