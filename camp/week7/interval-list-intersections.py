class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        top, bottom = 0, 0
        ans = []
        n, m = len(firstList), len(secondList)
        while top < n and bottom < m :
            # max starting , min ending indexes chosen
            low = max(firstList[top][0],secondList[bottom][0])
            high = min(firstList[top][1],secondList[bottom][1])

            # if there is intersection add
            if high >= low: ans.append([low,high])

            if firstList[top][1] > secondList[bottom][1]: bottom += 1
            else: top += 1
        return ans