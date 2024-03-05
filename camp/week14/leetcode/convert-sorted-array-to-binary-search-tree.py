# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left,right):
            if left > right:
                return None
            mid =( right + left)//2
            lnode = helper ( left, mid - 1 )
            rnode = helper ( mid + 1 , right )
            return TreeNode(nums[mid], lnode ,rnode)
        
        return helper(0,len(nums)-1)