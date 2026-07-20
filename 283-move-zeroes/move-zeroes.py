# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j += 1

# class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     next_non_zero = 0

    #     for current in range(len(nums)):
    #         if nums[current] != 0:
    #             nums[next_non_zero], nums[current] = nums[current], nums[next_non_zero]
    #             next_non_zero += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1