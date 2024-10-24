class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # can you reach targets before the ghosts
        #  first calculate how much time it takes for the ghosts and you to get to your destination
        # compare
        my_time  = abs(target[0]) + abs(target[1])
        for cords in ghosts:
            ghost_time = abs(target[0] - cords[0]) + abs(target[1] - cords[1])
            # print(my_time, ghost_time)
            if my_time >= ghost_time:
                return False
        return True 