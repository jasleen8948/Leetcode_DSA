# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list(set(nums1) & set(nums2))



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        ans = set()

        for num in nums2:
            if num in s:
                ans.add(num)

        return list(ans)