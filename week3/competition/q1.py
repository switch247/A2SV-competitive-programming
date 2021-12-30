#15min
n=4
for i in range(1,(2*n)+1,2):
    for j in range(1,2*n-i+1,2):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    print()


for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='')
    print()


