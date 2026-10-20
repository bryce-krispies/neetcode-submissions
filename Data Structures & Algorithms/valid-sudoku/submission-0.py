class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                cursor = board[i][j]

                if cursor == ".":
                    continue

                if cursor in rows[i] or cursor in cols[j] or cursor in squares[(i // 3, j // 3)]:
                    return False

                rows[i].add(cursor)
                cols[j].add(cursor)
                squares[(i // 3, j // 3)].add(cursor)

        return True