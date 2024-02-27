# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if p == None and q == None:
                return True
            elif p and q and p.val == q.val:
                # right of one is left of the other
                m = helper(p.left, q.right)
                n = helper(p.right, q.left)
                return m and n
            else:
                return False

        return helper(root.left, root.right)