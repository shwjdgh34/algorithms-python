class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_benefit = 0
        for price in prices:
            if min_price > price:
                min_price = price
            if max_benefit < price - min_price:
                max_benefit = price - min_price
        return max_benefit

        