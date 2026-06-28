class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False

        return True

# # # class Solution:
# # #     def isAnagram(self, s: str, t: str) -> bool:
# # #         return sorted(s)==sorted(t)

# # class Solution:
# #     def isAnagram(self, s: str, t: str) -> bool:
# #         freq = {i: 0 for i in range(26)}
# #         if len(s)!=len(t):
# #             return false
# #         for i in range(len(s)):
# #             i+=1
# #             # freq[s[i]-'a']++(cpp)
# #             # freq[t[i]-'a']--
# #             # if i=0 to 26 
# #             # freq[i]==1

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_clean = ""
#         t_clean = ""

#         for ch in s:
#             if ch.isalnum():
#                 s_clean += ch.lower()

#         for ch in t:
#             if ch.isalnum():
#                 t_clean += ch.lower()

#         return sorted(s_clean) == sorted(t_clean)
