# time n, space 1

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)-1):
            if(prices[i] < prices[i+1]):
                m += prices[i+1] - prices[i]
        return m