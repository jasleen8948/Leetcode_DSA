# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         result = []

#         for i in range(len(nums) - 2):

#             # Skip duplicate first elements
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             left = i + 1
#             right = len(nums) - 1

#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]

#                 if total == 0:
#                     result.append([nums[i], nums[left], nums[right]])

#                     # Skip duplicates
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1

#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1

#                     left += 1
#                     right -= 1

#                 elif total < 0:
#                     left += 1

#                 else:
#                     right -= 1

#         return result


class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])

                    left_val = nums[l]
                    right_val = nums[r]

                    while l < r and nums[l] == left_val:
                        l += 1
                    while l < r and nums[r] == right_val:
                        r -= 1

        return ans