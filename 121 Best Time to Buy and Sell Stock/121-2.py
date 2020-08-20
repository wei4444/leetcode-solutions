# time n, space 1

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        lo = 0
        hi = 0
        for i in range(1, len(prices)):
            if(prices[i] < prices[lo]):
                lo = i
                hi = i
            if(prices[i] > prices[hi]):
                hi = i
            if(prices[hi] - prices[lo] > m):
                m = prices[hi] - prices[lo]
        return m


print(Solution().maxProfit([7,1,5,3,6,4]))