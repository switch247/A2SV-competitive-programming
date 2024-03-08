n = int(input())
prices = list(map(int, input().split()))
prices.sort()

q = int(input())
def pos (target):
    l, r = 0, n-1
    ans = 0
    while l<=r:
        mid = (l+r)//2
        if prices[mid]<=target:
            ans = mid +1
            l = mid+1
        else:
            r = mid-1
    return ans
    # tot =  j
    # for i,price in enumerate(prices):
    #     if tot < price:
    #         return i
    # return n

for i in range(q):
    z = int(input())
    print(pos(z))



























