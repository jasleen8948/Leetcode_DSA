class Solution:
    def longestPalindrome(self, s):
        # Transform string to handle odd and even length palindromes
        t = '^#' + '#'.join(s) + '#$'
        n = len(t)

        p = [0] * n
        center = right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            # Expand around center
            while t[i + (1 + p[i])] == t[i - (1 + p[i])]:
                p[i] += 1

            # Update center and right boundary
            if i + p[i] > right:
                center = i
                right = i + p[i]

        # Find longest palindrome
        max_len = max(p)
        center_index = p.index(max_len)

        start = (center_index - max_len) // 2

        return s[start:start + max_len]