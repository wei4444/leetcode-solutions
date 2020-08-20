# counter hash table
# time n, space 1

import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        c = collections.Counter()
        for i in range(len(s)):
            c[s[i]] += 1
            c[t[i]] -= 1
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if(c[i] != 0):
                return False
        
        return True

print(Solution().isAnagram('cat', 'tac'))
print(Solution().isAnagram('cat', 'rat'))