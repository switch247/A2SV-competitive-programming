# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: return
        # ans = 0
        mx, mn = float('-inf'), float('inf')
        def trav(root,min_val,max_val):
            if not root:
                x = abs(max_val - min_val)
                # print(min_val,max_val, '**',x)
                return x
            # print(min_val,max_val)
            max_val = max( max_val, root.val)
            min_val = min( min_val, root.val)
            
            left = trav(root.left, min_val, max_val)
            right = trav(root.right, min_val, max_val)
            ans = max(left, right)
            return ans
        return trav(root,mn, mx)
        