# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums,left,right):
            if left > right:
                return None
            max_val = max(nums[left:right+1])
            maxi_idx = nums.index( max_val )
            root = TreeNode(max_val)
            root.left = helper(nums,left, maxi_idx -1)
            root.right = helper(nums,maxi_idx + 1, right)
            return root
        return helper(nums, 0,len(nums)-1)

        # nums to the left of a chosen number become left children of that number and nums on the right become right children
        # 321 [6] 05 (max num as parent)
        # 321 left 05 right
        # repeate for each section
