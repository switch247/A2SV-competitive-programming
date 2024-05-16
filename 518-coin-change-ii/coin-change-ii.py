class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amounts= [0]* (amount+1)
        amounts[0] =1
        for coin in coins:
            for x in range(coin, amount+1):
                diff = (x-coin)
                # diff = ways to reach x
                # x = coin + diff
                amounts[x] += amounts[diff]
            # print(amounts)
        return amounts[amount]