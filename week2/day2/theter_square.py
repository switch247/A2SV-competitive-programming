def theatreSquare(n,m ,a):
    row=0
    colum= 0
    if n%k ==0:
        row= n//a
    else:
        row= n//a +1
    if m%k==0:
        colum=m//a
    else:
        colum=m//a +1
    print(col*row)
theatreSquare(4,4,6)
#flag posts== tiles on the floor total tiles = no tiles placed vertically*tiles places horizontally
#length%a== how many you can fit with out exceeding
