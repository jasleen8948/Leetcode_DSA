# class Solution:
#     def firstUniqChar(self, s: str) -> int:

#         for i in range(len(s)):
#             if s.count(s[i]) == 1:
#                 return i

#         return -1
class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}

        # Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Find first unique character
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1