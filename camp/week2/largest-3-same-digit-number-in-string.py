class Solution:
    def largestGoodInteger(self, num: str) -> str:
        x = []
        for i in range(2,len(num)):
            if num[i-1] == num[i-2] and num[i] == num[i-2]:
                x.append(num[i])
        x.sort()
        # print(x)
        return x[-1] * 3 if x else ""
