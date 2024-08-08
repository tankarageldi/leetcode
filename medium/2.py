# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):          
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = 0
        right = 0
        multi = 1
        while l1 and l2:
            left += (l1.val)*multi
            l1=l1.next
            right += (l2.val)*multi
            l2=l2.next
            multi = multi * 10
        total = right + left
        s = str(total)
        ans = [int(digit) for digit in reversed(s)]
        if not l1 or l2:
            return ListNode(0)
        i = 0
        while l1 and i < len(ans): 
            l1.val = ans[i]
            i += 1
        return l1
        
        

l1 = [2,4,3]
l2 = [5,6,4]
sol = Solution()
print(sol.addTwoNumbers(l1,l2))
