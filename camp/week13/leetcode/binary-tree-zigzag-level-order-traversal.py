# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # this is easier to understand
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        parents = deque([root])
        flag = True
        result = []
        while parents:
            size = len(parents)
            level = deque()

            for _ in range(size):
                current = parents.popleft()
                if flag:
                    level.append(current.val)
                else:
                    level.appendleft(current.val)
                # children become parents
                if current.left:
                    parents.append(current.left)
                if current.right:
                    parents.append(current.right)
            # print(level)
            flag = not flag
            result.append(level)
        
        return result
    # def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     visited = []
    #     q = deque()
    #     q.append((0,root)) 
    #     d = defaultdict(deque)
    #     while q:
    #         level, cur = q.popleft()
    #         if not cur:
    #             break        
    #         visited.append((level,cur.val))
    #         if level%2:
    #             d[level].appendleft(cur.val)
    #         else:
    #             d[level].append(cur.val)

    #         if cur.left or cur.right:
    #             if cur.left:
    #                 q.append((level+1,cur.left))
    #             if cur.right:
    #                 q.append((level+1,cur.right))
    #     ans= []
    #     for i in sorted(d.keys()):
    #         ans.append((d[i]))
    #     # print(visited)
    #     # print(d)
    #     return ans
