# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root,x,ans):
            if not root:
                return ans
            ans.append(root)
            if root.val == x.val:
                return ans
            elif x.val > root.val:
                return search(root.right,x,ans)
            else:
                return search(root.left,x,ans)
        
        l = search(root,p,[])
        r = search(root,q,[])
        ans = None
        for a, b in zip(l,r):
            if a.val==b.val:
                ans = a
        # print(l,r, sep='\n')
        return ans
