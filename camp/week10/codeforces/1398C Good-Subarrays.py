t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input()))
    d={0:1}
    rsum = 0
    ans = 0
    for i in range(n):
        rsum += arr[i]
        # s = i + 1 
        goal = rsum - (i + 1)
        ans +=  d.get(goal, 0)
        d[goal] = d.get(goal, 0) + 1
   
    print(ans)
