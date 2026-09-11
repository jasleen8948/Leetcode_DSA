class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = 0

        for first in range(1, 10):
            for second in range(10):
                for last in range(0, 10, 2):

                    if freq[first] == 0:
                        continue

                    freq[first] -= 1

                    if freq[second] == 0:
                        freq[first] += 1
                        continue

                    freq[second] -= 1

                    if freq[last] > 0:
                        ans += 1

                    freq[second] += 1
                    freq[first] += 1

        return ans