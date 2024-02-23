class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastidx = {}
        for i, ch in enumerate(s):
            lastidx[ch] = i
        # print(lastidx)
        i = 0
        ans = []
        while i < len(s):
            # print(s[i], lastidx[s[i]])
            end, j = lastidx[s[i]], i + 1
            while j < end: # eval last idx of those between [i+1,end]
                # some characters last index may not be in in [i, end] so acount for that
                # a b a b {a:2, b:3} but b is with in [i,end]([0,2]) and its last idx is 3 so push the end
                # 0 1 2 3
                end = max(lastidx[s[j]], end )
                j += 1
            sublen = end - i + 1 # substring length
            ans.append(sublen)
            i = end + 1

        return ans
        

        
          