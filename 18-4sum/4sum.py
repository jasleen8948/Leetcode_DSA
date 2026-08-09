# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         n = len(nums)
#         ans = []

#         for i in range(n - 3):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             for j in range(i + 1, n - 2):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue

#                 left = j + 1
#                 right = n - 1

#                 while left < right:
#                     total = nums[i] + nums[j] + nums[left] + nums[right]

#                     if total == target:
#                         ans.append([nums[i], nums[j], nums[left], nums[right]])

#                         left += 1
#                         right -= 1

#                         while left < right and nums[left] == nums[left - 1]:
#                             left += 1

#                         while left < right and nums[right] == nums[right + 1]:
#                             right -= 1

#                     elif total < target:
#                         left += 1

#                     else:
#                         right -= 1

#         return ans



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            for j in range(i + 1, n):
                l, r = j + 1, n - 1

                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        return list(map(list, res))