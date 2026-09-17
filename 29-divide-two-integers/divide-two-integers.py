class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        a, b = abs(dividend), abs(divisor)
        ans = 0

        while a >= b:
            temp, multiple = b, 1

            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            ans += multiple

        if sign == -1:
            ans = -ans

        return min(max(ans, -2**31), 2**31 - 1)