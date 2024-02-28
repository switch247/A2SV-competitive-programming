# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def find(root,val):
            if not root :
                return
            if val < root.val:
                return find(root.left,val)
            elif val > root.val:
                return find(root.right,val)
            else:
                return root
        return find(root,val)
