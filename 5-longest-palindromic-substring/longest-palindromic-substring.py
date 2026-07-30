# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2:
#             return s
#         start = end = 0
#         def expand(left, right):
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return left + 1, right - 1
#         for i in range(len(s)):
#             l1, r1 = expand(i, i)       # Odd length
#             l2, r2 = expand(i, i + 1)   # Even length
#             if r1 - l1 > end - start:
#                 start, end = l1, r1
#             if r2 - l2 > end - start:
#                 start, end = l2, r2
#         return s[start:end + 1]

# BY DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    if length == 2 or dp[left + 1][right - 1]:
                        dp[left][right] = True

                        if length > max_len:
                            start = left
                            max_len = length

        return s[start:start + max_len]
