import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        min_price=10000
        for price in prices:
            min_price = min(min_price, price)
            
            profit = max(profit, price-min_price)
            
            
        if profit != 0:
            return profit
        else:
            return 0