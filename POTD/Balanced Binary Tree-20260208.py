# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lheight = self.height(root.left)
        rheight=self.height(root.right)
        if abs(lheight - rheight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self,node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)
