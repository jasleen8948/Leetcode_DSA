class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        ans = ['']

        for digit in digits:
            new = []
            for s in ans:
                for ch in mp[digit]:
                    new.append(s + ch)
            ans = new

        return ans
        