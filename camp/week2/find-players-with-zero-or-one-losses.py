from sortedcontainers import SortedList
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [ [] ,[] ]
        D = {}
        players = set()
        for winner,loser in matches:
            D[loser] = D.get(loser,0)  + 1
            players.update([ winner,loser])
            # print(players)

        # z = SortedList()
        # z.update(list(players))
        
        for player in players:
            # print(player)
            value =  D.get(player,0)
            if value==1:
                answer[1].append(player)
            elif value == 0:
                answer[0].append(player)
        answer[0].sort()
        answer[1].sort()

        return answer