# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         if len(s) != len(t):
#             return False

#         freq = {}

#         for ch in s:
#             freq[ch] = freq.get(ch, 0) + 1

#         for ch in t:
#             if ch not in freq:
#                 return False

#             freq[ch] -= 1

#             if freq[ch] < 0:
#                 return False

#         return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
        
#         countS,countT={},{}
#         for i in range (len(s)):
#             countS[s[i]]=1 + countS.get(s[i],0)
#             countT[t[i]]=1 + countT.get(t[i],0)
#         for c in countS:
#             if countS[c]!=countT.get(c,0):
#                 return False
#         return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
