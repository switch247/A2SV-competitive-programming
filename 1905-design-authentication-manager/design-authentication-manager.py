class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.auth = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.auth[tokenId] = currentTime + self.timeToLive
        # print(tokenId ,self.auth[tokenId],"added")
        # tokenId:expires at


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.auth:
            expire_time  = self.auth[tokenId]
            
            if expire_time > currentTime:
                self.auth[tokenId] = currentTime + self.timeToLive
        #         print("renewed")
        #     else:
        #         print("expired")
        # else:
        #     print('not found')

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for expire_time in self.auth.values():
            if expire_time > currentTime:
                count+=1
        # print("count", count)
        return count

# Note that if a token expires at time t, and another action happens on time t (renew or countUnexpiredTokens), the expiration takes place before the other actions.

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)