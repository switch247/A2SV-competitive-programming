# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        s = defaultdict(lambda:0)
        def helper(root):
            if not root:
                return
            s[root.val]+=1
            helper(root.left)
            helper(root.right)
        
        helper(root)
        c = sorted([[mod,k] for k,mod in s.items()],reverse=True)
        # print(c)
        ans= [c[0][1]]

        for i in range(1, len(c)):
            if c[i][0] != c[0][0]:
                break
            ans.append( c[i][1] )
             
        return ans