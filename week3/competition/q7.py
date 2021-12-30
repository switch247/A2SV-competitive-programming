#14
x={}
x.update({'I':  1,
'V'      :       5,
'X'       :      10,
'L'        :     50,
'C'      :       100,
'D'     :      500,
'M'    :     1000
})
#print(x.values())
#s=list(map(str,input().split()))
s = list("LVIII")
tot=0
previous=0
#'IV'= 4,'IX'=9
# IV = V-I B/C I<V 
# VI= V+I /B V<I
#FROM RIGHT TO LEFT
for i in range(len(s)-1, -1, -1):
    if x[s[i]] >= previous:
        tot += x[s[i]]
    else:
        tot -= x[s[i]]
    
    previous = x[s[i]]
    #previous == 0,i,i_1,i-2 updated each time
 
print(tot)

