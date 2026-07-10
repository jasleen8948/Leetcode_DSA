class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            a=str(i)
            if len(a)%2==0:
                sum+=1
           
        return sum