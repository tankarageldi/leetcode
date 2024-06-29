class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        ans = []
        self.inOrder(root,ans)
        return ans

    def inOrder(self,root,ans):
        if root:
            self.inOrder(root.left,ans)
            ans.append(root.val)
            self.inOrder(root.right,ans)