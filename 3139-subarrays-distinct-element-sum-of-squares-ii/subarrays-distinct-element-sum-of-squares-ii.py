class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = 0
        total = 0

        def update(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0

            if ql <= l and r <= qr:
                old = tree[node]
                tree[node] += r - l + 1
                lazy[node] += 1
                return old

            mid = (l + r) // 2

            if lazy[node]:
                v = lazy[node]
                tree[node * 2] += v * (mid - l + 1)
                tree[node * 2 + 1] += v * (r - mid)
                lazy[node * 2] += v
                lazy[node * 2 + 1] += v
                lazy[node] = 0

            old = 0
            if ql <= mid:
                old += update(node * 2, l, mid, ql, qr)
            if qr > mid:
                old += update(node * 2 + 1, mid + 1, r, ql, qr)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]
            return old

        def query_add(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0

            if ql <= l and r <= qr:
                old = tree[node]
                length = r - l + 1
                tree[node] += length
                lazy[node] += 1
                return old

            mid = (l + r) // 2
            if lazy[node]:
                v = lazy[node]
                tree[node * 2] += v * (mid - l + 1)
                tree[node * 2 + 1] += v * (r - mid)
                lazy[node * 2] += v
                lazy[node * 2 + 1] += v
                lazy[node] = 0

            old = 0
            if ql <= mid:
                old += query_add(node * 2, l, mid, ql, qr)
            if qr > mid:
                old += query_add(node * 2 + 1, mid + 1, r, ql, qr)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]
            return old

        for i, x in enumerate(nums):
            p = last.get(x, -1)

            old_sum = query_add(1, 0, n - 1, p + 1, i)
            total = (total + 2 * old_sum + i - p) % MOD
            ans = (ans + total) % MOD
            last[x] = i

        return ans