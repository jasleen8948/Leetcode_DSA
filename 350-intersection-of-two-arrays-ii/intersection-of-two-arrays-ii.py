# class Solution:
#     def intersect(self, nums1, nums2):
#         freq = {}

#         # Count frequency of nums1
#         for num in nums1:
#             if num in freq:
#                 freq[num] += 1
#             else:
#                 freq[num] = 1

#         ans = []

#         # Find intersection
#         for num in nums2:
#             if num in freq and freq[num] > 0:
#                 ans.append(num)
#                 freq[num] -= 1

#         return ans



from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        ans = []

        for num in nums2:
            if count[num] > 0:
                ans.append(num)
                count[num] -= 1

        return ans