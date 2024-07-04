
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mod = head.next
        current = mod

        while current:
            sum = 0
            while current.val != 0:
                sum += current.val
                current = current.next
            mod.val = sum
            current = current.next
            mod.next = current
            mod = mod.next
        return head.next

    



