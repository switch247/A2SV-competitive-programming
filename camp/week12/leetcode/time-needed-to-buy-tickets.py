class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        tickets = deque([[i,v] for i,v in  enumerate(tickets)])
        time = 0
        print(tickets)

        while tickets:
            time+=1
            z = tickets.popleft()
            if z[-1]!=1:
                z[-1]-=1
                tickets.append(z)
            else:
                if z[0]==k: return time
            # print(i, tickets)
        return time
