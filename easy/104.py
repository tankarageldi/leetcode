
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1 
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return max(left_height,right_height) + 1
                 