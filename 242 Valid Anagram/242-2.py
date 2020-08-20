# sorting
# time nlogn, space n

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        s1 = sorted([c for c in s])
        t1 = sorted([c for c in t])
        return s1 == t1

print(Solution().isAnagram('cat', 'tac'))
print(Solution().isAnagram('cat', 'rat'))