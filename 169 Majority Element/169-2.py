# more concise
# time n, space n

import collections
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return max(c.keys(), key=c.get) # get key with max value

print(Solution().majorityElement([2,3,3]))