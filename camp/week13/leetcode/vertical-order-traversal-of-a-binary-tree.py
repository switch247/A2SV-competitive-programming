# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        parents = deque([(0,root)])
        flag = True
        result = []
        
        while parents:
            size = len(parents)
            level = []
            for _ in range(size):
                order , current = parents.popleft()
                if flag:
                    level.append((order,current.val))
                # else:
                #     level.appendleft((order,current.val))
                # children become parents
                if current.left:
                    parents.append((order -1, current.left))
                if current.right:
                    parents.append((order+1, current.right))
            # print(level)
            # flag = not flag
            level.sort(key=lambda x : x[1])
            result.append(level)
        
        d = defaultdict(list)
        for level in result:
            for order, val in level:
                d[order].append(val)
        ans = []
        for key in sorted(d.keys()):
            ans.append(d[key])
        # print(result)
        return ans
