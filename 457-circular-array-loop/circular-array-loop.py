class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            runner = i
            visited = set()
            flag = (nums[i] > 0)
            while (nums[runner] > 0) == flag and (n + runner + nums[runner]) % n != runner:
                # find next position of runner
                runner = (n + runner + nums[runner]) % n
                if runner in visited:
                    return True
                
                visited.add(runner)


        return False



        # n = len(nums)
        # visited = set()
        # for i in range(n):
        #     if i not in visited:
        #         loop = set()
        #         while True:
        #             if i in loop:
        #                 return True
        #             visited.add(i)
        #             loop.add(i)
        #             prev,i= i,(i+nums[i])%n
                    
        #             if i == prev:
        #                 break
        #             if (nums[prev]<0 and nums[i]>0) or (nums[i]<0 and nums[prev]>0):
        #                 break
        # return False