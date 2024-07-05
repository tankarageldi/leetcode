# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        result = [-1,-1]

        # minimum distance set to infinite. 
        min_distance = float("inf")
        # pointers to track.
        critical_points=[]
        prev = head
        curr = head.next
        index = 1

        while curr.next: 
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                critical_points.append(index) 
            curr_index += 1
            prev = curr
            curr = curr.next

        if len(critical_points) < 2:
            return [-1,-1]

        max_distance = critical_points[-1] - critical_points[0]

        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])

        return [min_distance,max_distance]

        