class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        x= [i.split(' ') for i in paths]
        d ={}
        # content:[pathtofile,]
        for i in x:
            p = i[0]
            z = i[1:]
            for j in z:
                inj = len(j)
                ind = j.index('(')
                content = j[ind:]
                fil =  j[:ind]
                if content not  in d:
                    d[content] = [p+'/'+fil]
                else:
                    d[content] = d.get(content,[]) +[p+'/'+fil]
        answer = []
        for i,v in d.items():
            if len(v) > 1:
                answer.append(v)

        # sorted(answer,key=len , reverse=True)
        return answer
        