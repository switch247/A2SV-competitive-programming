# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return []
            left = inorder(root.left)
            right = inorder(root.right)
            ans = []
            ans.extend(left)
            ans.append(root.val)
            ans.extend(right)
            return ans
        
        return inorder(root)[k-1]
