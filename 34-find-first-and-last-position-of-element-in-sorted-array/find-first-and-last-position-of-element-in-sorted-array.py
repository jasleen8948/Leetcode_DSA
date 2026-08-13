class Solution:
    def searchRange(self, nums, target):
        l = bisect_left(nums, target)
        r = bisect_right(nums, target) - 1
        
        return [l, r] if l <= r else [-1, -1]