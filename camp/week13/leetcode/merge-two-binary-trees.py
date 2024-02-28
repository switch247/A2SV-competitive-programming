# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if (not root1) and (not root2):
            return
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            r1 = root1.val
            r2 = root2.val
            root1.val = r1+r2
            # root2.val = r1+r2
        
        left = self.mergeTrees(root1.left, root2.left)
        right = self.mergeTrees(root1.right, root2.right)
        
        root1.left = left
        # root2.left = left

        root1.right = right
        # root2.right = right

        return root1