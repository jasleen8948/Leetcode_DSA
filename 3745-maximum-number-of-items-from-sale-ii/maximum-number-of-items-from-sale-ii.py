
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)

        for f, p in items:
            freq[f] += 1

        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                freq[i] += freq[j]

        items.sort(key=lambda x: x[1])
        mn = items[0][1]
        ans = 0

        for f, p in items:
            if p >= 2 * mn:
                break

            take = min(freq[f] - 1, budget // p)
            ans += 2 * take
            budget -= take * p

        return ans + budget // mn
