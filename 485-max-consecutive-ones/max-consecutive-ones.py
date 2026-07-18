# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         count = 0
#         max_count = 0
#         for num in nums:
#             if num == 1:
#                 count += 1
#                 max_count = max(max_count, count)
#             else:
#                 count = 0
#         return max_count

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = cur = 0
        for x in nums:
            if x: #shorter way of writing if x==1:
                cur += 1
                if cur > ans:
                    ans = cur
            else:
                cur = 0

        return ans