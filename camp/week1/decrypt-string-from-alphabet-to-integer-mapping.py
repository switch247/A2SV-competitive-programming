class Solution:
    def freqAlphabets(self, s: str) -> str:
        # print(s.split('#'))
        #  "1326#" ()=> ['1326', '']
        # xx# 10-26 double digit
        # x 1-9
        # chr() 
        # 97 == a  (1)=>{97} so + 96
        # print( chr(97), chr(96+25) )
        answer = ''
        temp = ''
        for i in s:
            if i == '#':
                # eval temp
                x = chr( int( temp[-2:] ) + 96 )
                # print(x, temp[-2:])
                copy = temp[:-2] 
                for i in copy:
                    t = chr( int( i ) + 96 )
                    # print(t, i)
                    answer += t              
                answer += x
                temp  = ''
            else:
                temp += i
        
        for i in temp:
            answer += chr( int(i) + 96)
        return  answer

        # "abcdefghi a` klmnopqrstuvwxyz"
        # "abcdefghi j klmnopqrstuvwxyz"
        