# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         c=0
#         while(n>0):
#             if(n%2==1):
#                 c+=1

#             n=n//2
#         return c

# # hamming weight is the number of 1 in a bit no.
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count