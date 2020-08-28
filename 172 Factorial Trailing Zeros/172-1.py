# time log(n), space 1

class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 5
        r = 0
        while(i <= n):
            r += n // i
            i *= 5
        return r

print(Solution().trailingZeroes(200))