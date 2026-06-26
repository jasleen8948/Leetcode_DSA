# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         x, y = m - 1, n - 1
#         for z in range(m + n - 1, -1, -1):
#             if x < 0:
#                 nums1[z] = nums2[y]
#                 y -= 1
#             elif y < 0:
#                 break
#             elif nums1[x] > nums2[y]:
#                 nums1[z] = nums1[x]
#                 x -= 1
#             else:
#                 nums1[z] = nums2[y]
#                 y -= 1


class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1