# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # better approach
        def help(node, val):
            if not node:
                return 0
            val = val*10 + node.val
            if not (node.left or node.right):
                # leaf 
                return val  

            # 485 + 491 |+ 40 
            return help(node.left, val) + help(node.right, val)
        return help(root, 0)
        # x = []
        # def trav(root,ans):
        #     if not root:
        #         return
        #     cpy = ans[:]
        #     cpy.append(str(root.val))
        #     if not root.left and not root.right:
        #         # leaf
        #         x.append(cpy)
        #     else:
        #         l = trav(root.left,cpy)
        #         r = trav(root.right,cpy)
        
        # trav(root,[])
        # sum = 0
        # for i in range(0, len(x)):
        #     sum+= int(''.join(x[i]))

        # # print(x, sep='\n')
        # return sum
