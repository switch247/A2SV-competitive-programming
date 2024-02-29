# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # better approach
        def help(root, min_val, max_val):
            if not root:
                return True
            if min_val < root.val < max_val:
                # nodes on the left can't be greater than their parents 
                left = help(root.left, min_val,  root.val)
                # nodes on the right can't be lesser than their parents 
                right = help(root.right,  root.val, max_val)
                return left and right 
            else:
                return False
        return help(root, float('-inf'), float('inf'))
        # def inorder(root):
        #     if not root:
        #         return []
        #     left = inorder(root.left)
        #     right = inorder(root.right)
        #     ans = []
        #     ans.extend(left)
        #     ans.append(root.val)
        #     ans.extend(right)
            
        #     return ans
        
        # arr = inorder(root)
        # for i in range(1,len(arr)):
        #     if arr[i] <= arr[i-1]:
        #         return False
        # return True


        
