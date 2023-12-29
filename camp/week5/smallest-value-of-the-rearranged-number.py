from functools import cmp_to_key
class Solution:
    def smallestNumber(self, num: int) -> int:
        def compare(x, y):
            return int( y + x ) - int( x+ y ) 
        
        if num < 0:
            num = [ i for i in str(num)[1:] ]
            num = sorted(num, key = cmp_to_key(compare))
            return -int(''.join(num))
        else:
            num = [ i for i in str(num) ]
            #  does not contain any leading zeros.
            zeros = num.count('0')
            num = sorted(num, key = cmp_to_key(compare), reverse= True)
            # remove trailing zero
            num = [i for i in str(int(''.join(num)))]
            if zeros > 0:
                new = [num[0]] 
                # add the zeros back 
                for i in range(zeros): new.append('0')
                for i in num[1:]: new.append(i)
                num = new
        
            return int(''.join(num))
        
        