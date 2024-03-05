# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        root.val= 0
        dic=defaultdict(list)
        def dfs(root,level):
            if not root.left and not root.right:
                return 
            n = root.val
            if root.left:
                pos = (2*n)+1
                root.left.val = pos
                dic[level+1].append( pos )
                dfs(root.left,level+1)
            if root.right:
                pos = (2*n)+2
                root.right.val = pos
                dic[level+1].append(pos)
                dfs(root.right,level+1)
        dfs(root,0)
        # print(dic)
        ans = 1
        for v in dic.values():
            ans = max(ans , ( max(v) - min(v) )+1 )
        # print(root, sep='\n')
        return ans

    #          0
    #         1 2 
    #       3 4 5 6
    # 7 8 9 10 11 12 13 14
    # 15 16 ...
    # left = 2* parent+1
    # right = 2*parent+2
    # start root must be 0