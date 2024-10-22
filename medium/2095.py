# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        fast = head
        slow = head
        prev = None
        while fast and fast.next: 
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = slow.next
            slow.next = None
        else:
            return None
        return head