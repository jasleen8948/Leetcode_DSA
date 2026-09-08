# class Solution:
#     def countCommas(self, n: int) -> int:
#         ans = 0
        
#         for i in range(1, n + 1):
#             ans += f"{i:,}".count(",")
        
#         return ans

class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        p = 1000

        while p <= n:
            ans += n - p + 1
            p *= 1000

        return ans