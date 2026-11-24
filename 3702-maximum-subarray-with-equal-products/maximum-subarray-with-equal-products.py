class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]

                from math import gcd
                lcm = 1

                for k in range(i, j + 1):
                    lcm = lcm * nums[k] // gcd(lcm, nums[k])

                if prod == lcm * __import__('functools').reduce(
                    gcd, nums[i:j+1]
                ):
                    ans = max(ans, j - i + 1)

        return ans