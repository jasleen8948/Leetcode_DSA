class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         ans = len(nums)

#         for i in range(len(nums)):
#             ans ^= i ^ nums[i]

#         return ans