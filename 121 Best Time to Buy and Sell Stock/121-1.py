# brute force, TLE
# time n^2, space 1

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                d = prices[j] - prices[i]
                if(d > m):
                    m = d
        return m

print(Solution().maxProfit([7,1,5,3,6,4]))