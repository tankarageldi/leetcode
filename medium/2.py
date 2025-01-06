# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):          
        self.val = val
        self.next = next
class Solution:
    # did it myslf
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ''
        second = ''
        while l1:
            first = str(l1.val) + first
            l1 = l1.next
        while l2:
            second = str(l2.val) + second
            l2 = l2.next
        
        total = int(first) + int(second)
        total = total
        dummy = ListNode()
        curr = dummy
        for digit in str(total)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
        
        return dummy.next
        
     ## optimal solution
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

        
        
        
        
