class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5 , 'X':10 , 'L':50 ,'C' :100 ,'D': 500 ,'M':1000}
        total = d[s[-1]]
        if len(s)<2: return total
        for i in range(len(s)-2,-1,-1):
            print(total)
            if d[s[i]] >= d[s[i+1]]:
                total+=d[s[i]]
            else:
                total-=d[s[i]]

        return total

# v5
# vi 6  
# iv 4


