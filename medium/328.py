# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = head.next
        holder = second

        while first.next and second.next:
            first.next = first.next.next
            second.next = second.next.next

            first = first.next.next
            second = second.next.next
        first.next = holder
        return first
