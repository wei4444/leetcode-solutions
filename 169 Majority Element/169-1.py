# time n, space n

import collections
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums) // 2
        c = collections.Counter()
        for n in nums:
            c[n] += 1
        
        for n in c.keys():
            if(c[n] > l):
                return n

print(Solution().majorityElement([2,3,3]))