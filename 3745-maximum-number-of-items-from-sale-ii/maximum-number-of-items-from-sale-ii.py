
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Count frequency of each factor
        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count how many factors are multiples of each factor
        gain = freq[:]

        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                gain[i] += freq[j]

        # Sort items by price
        items.sort(key=lambda x: x[1])

        min_price = items[0][1]
        ans = 0

        # Buy items that provide an extra free item
        for factor, price in items:
            if price >= 2 * min_price:
                break

            free_count = gain[factor] - 1

            if free_count <= 0:
                continue

            take = min(free_count, budget // price)

            ans += 2 * take
            budget -= take * price

        # Spend remaining budget on cheapest items
        ans += budget // min_price

        return ans
