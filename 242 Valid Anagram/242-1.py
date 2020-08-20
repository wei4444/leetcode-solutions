# time n^2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        while(len(s) > 0):
            if(s[0] in t):
                i = t.find(s[0])
                t = t[:i] + t[i+1:]
                s = s[1:]
            else:
                return False
        
        return True

print(Solution().isAnagram('cat', 'tac'))
print(Solution().isAnagram('cat', 'rat'))