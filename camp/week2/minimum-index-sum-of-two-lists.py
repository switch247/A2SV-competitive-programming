class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # answer  = 'word', index_sum
        answer = []
        for index, word in enumerate(list1):
            if word in list2:
                # print(word, index  ,  list2.index(word))
                index_sum =  index  +  list2.index(word) 
                answer.append(( index_sum,word))
        answer.sort()
        # print(answer)
        new = [ answer[0][1] ]
        t = answer[0][0]
        for i in  range(1, len(answer)):
            if answer[i][0] != t:
                break
            new.append(answer[i][1]) 
            
        return new

        