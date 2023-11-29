class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # 3 a + 3 = num
        a =  ( num - 3 ) / 3 
        print(a, a % 10)
        if  a   == int(a):
            # it is an int or x.0 doe
            return [int(a), int(a+1), int(a+2)]
        else:
            return []
            