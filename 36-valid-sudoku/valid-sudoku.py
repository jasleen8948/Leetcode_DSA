# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = [set() for _ in range(9)]
#         cols = [set() for _ in range(9)]
#         boxes = [set() for _ in range(9)]

#         for r in range(9):
#             for c in range(9):
#                 num = board[r][c]

#                 if num == ".":
#                     continue

#                 box = (r // 3) * 3 + (c // 3)

#                 if num in rows[r] or num in cols[c] or num in boxes[box]:
#                     return False

#                 rows[r].add(num)
#                 cols[c].add(num)
#                 boxes[box].add(num)

#         return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1')
                    boxIndex = (i // 3) * 3 + (j // 3)
                    if rows[i][num] or cols[j][num] or boxes[boxIndex][num]:
                        return False
                    rows[i][num] = cols[j][num] = boxes[boxIndex][num] = True
        return True