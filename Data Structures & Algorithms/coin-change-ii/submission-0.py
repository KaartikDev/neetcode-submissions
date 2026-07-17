class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        row = [None] * len(coins)
        table = [row.copy() for _ in range(amount+1)]
        def dp(amt, coinIndex):
            if amt == 0:
                return 1
            if coinIndex >= len(coins) or amt < 0:
                return 0
            if table[amt][coinIndex] is not None:
                return table[amt][coinIndex]
            
            take = dp(amt-coins[coinIndex],coinIndex)
            skip = dp(amt,coinIndex+1,)
            table[amt][coinIndex] = take+skip
            return table[amt][coinIndex]

        return dp(amount,0)

        