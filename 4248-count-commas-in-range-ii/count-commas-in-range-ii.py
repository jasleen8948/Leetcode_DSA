# class Solution:
#     def countCommas(self, n: int) -> int:
#         k = (len(str(n)) - 1) // 3 # int(log10(n)) // 3 
#         return k * (n + 1) - (1000**(k + 1) - 1000) // 999

class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        x = 1000

        while x <= n:
            ans += n - x + 1
            x *= 1000

        return ans