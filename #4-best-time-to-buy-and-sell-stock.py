import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        leastvalue = math.inf


        for i in range(len(prices)):
            profit = prices[i] - leastvalue

            if profit > max_profit:
                max_profit = profit

            if prices[i] < leastvalue:
                leastvalue = prices[i]

        return max_profit