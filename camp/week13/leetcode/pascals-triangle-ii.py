class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(old,i):
            if i ==0: old.append(1)
            # 
            if i==rowIndex:
                return old
            # 
            new = [ ]
            new.append(old[0])
            # old =[1,2,3,4, 5]
            for idx in range( len(old) ):
                # idx ==0 or
                if idx < len(old) -1:
                    new.append( (old[idx]+ old[idx+1]) )
                else:
                    new.append(old[idx])


            # print(new)
            return helper(new, i+1) 
        
        return helper([],0)

# 0 1 0
# x 1 1
# 0 1 1 0
# x 1 2 1
# 0 1 2 1 0
# x 1 3 3 1
# 0 1 3 3 1 0
# 