class Solution:
    def intersect(self, nums1, nums2):
        freq = {}

        # Count frequency of nums1
        for num in nums1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = []

        # Find intersection
        for num in nums2:
            if num in freq and freq[num] > 0:
                ans.append(num)
                freq[num] -= 1

        return ans