class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # player 1 score = player 1 score- player 2 score
        # if player 1 score>=0 player 1 won or is tied
        # player 1 chooses one that will maximize his own choice by minimizing the oponents choice
        # player can choose left or right
        
        cache = defaultdict( int ) 
        # use dictionary as dynamic programming table, to store the score gap

        def choose(left, right):
            if left==right:
                return nums[left] # when finished choosing
            if (left, right) in cache:
                # If this query has been computed before
                # directly return by cache table
                return cache[ (left, right) ]
            
            left_choose = nums[left] - choose(left+1, right)
            right_choose = nums[right] - choose(left,right-1)
            
            cache[ (left, right) ] = max( left_choose, right_choose)
            return cache[ (left, right) ]
        
        return choose(0,len(nums)-1 )>=0

            
           
            