class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        x = Counter(answers)
        print(x)
        ans = 0
        for i in x:
            if i==0:
                ans += x[i]
            elif (i+1) >= x[i]:
                #  2 2 2  2:3 =>3_3 (i+1)_x[i]
                # 10 10 10 10:3 => 11_3
                # print(i,x[i])
                ans += (i + 1)      
            else:   
                # 111 1:3 [ 3 rabits say that there is 2 of them ]
                # print(i,x[i],'?')
                # 3/2=> 1.5 ~ 2 , 2 types of rabits or two types of groups
                number_of_types = ceil(x[i]/(i + 1)) 
                ans += number_of_types *(i + 1)

        return ans
        