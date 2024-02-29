# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ans=[]
        # def inorder(root):
        #     if not root:
        #         return 
        #     left = inorder(root.left)
        #     ans.append(root.val)
        #     right = inorder(root.right)
        #     return 
        
        # inorder(root)
        # return ans[k-1]
        # ans = None
        ans = None
        def inorder(node):
            if node:
                # go to max left
                inorder(node.left)
                # k int points to 1st smaller even thought its the oposite
                nonlocal k 
                k -= 1
                if k == 0:
                    nonlocal ans
                    ans = node.val
                # go 1 right then max left
                inorder(node.right)
            
        inorder(root)
        return ans

        # same aproach iteratively
        # stack = []
        # curr = root

        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return curr.val
        #     curr = curr.right
        # return -1

