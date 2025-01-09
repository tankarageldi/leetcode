# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        left = head
        right = head.next

        while right:
            value = math.gcd(left.val,right.val)
            node = ListNode(value)

            left.next = node
            node.next = right

            left = right
            right = right.next
        return head



        