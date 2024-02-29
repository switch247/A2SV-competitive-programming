# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        x = []
        def trav(root,ans):
            if not root:
                return
            cpy = ans[:]
            cpy.append(str(root.val))
            if not root.left and not root.right:
                # leaf
                x.append(cpy)
            else:
                l = trav(root.left,cpy)
                r = trav(root.right,cpy)
        
        trav(root,[])
        sum = 0
        for i in range(0, len(x)):
            sum+= int(''.join(x[i]))

        # print(x, sep='\n')
        return sum