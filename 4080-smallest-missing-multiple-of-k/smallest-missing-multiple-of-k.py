# class Solution:
#     def missingMultiple(self, nums: List[int], k: int) -> int:
#         for i in range(1,len(nums)+2):
#             if k*i in nums:
#                 continue
#             else:
#                 return k*i


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)

        i = 1
        while True:
            multiple = k * i

            if multiple not in s:
                return multiple

            i += 1