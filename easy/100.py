class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # type: ignore
        l1 = self.traverse(p)
        l2 = self.traverse(q)
        print(l1)
        print(l2)
        if l1 == l2:
            return True
        return False



    def inOrder(self,node,result):
        if node:
            self.inOrder(node.left,result)
            result.append(node.val)
            self.inOrder(node.right,result)
    def traverse(self,root):
        result = []
        self.inOrder(root,result)
        return result



sol = Solution()
p = [1,null,1] # type: ignore
q = [1,1]

sol.isSameTree(q,p)
        