def countingValleys(steps, path):
    # Write your code here
    #if it changes from /- 'u' to 0 count valley
    d={'U':1, 'D':-1}
    valey=0
    level=0
    for i in path:
        level+=d[i]
        if level == 0 and i == 'U':
            valey+=1
    return valey

