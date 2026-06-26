# class Solution:
#     def reverseBits(self, n: int) -> int:
#         result = 0

#         for _ in range(32):
#             bit = n & 1
#             result = (result << 1) | bit
#             n >>= 1

#         return result

class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        b = b.zfill(32)      # 32 bits banao
        b = b[::-1]          # reverse
        return int(b, 2)     # binary -> decimal