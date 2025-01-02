# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0 

        rightTree = self.minDepth(root.right)
        leftTree = self.minDepth(root.left)

        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + rightTree
        if root.right is None:
            return 1 + leftTree
        
        return min(leftTree,rightTree) + 1

        