class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        n = len(word)

        def dfs(r, c, i):
            if i == n:
                return True

            if (
                r < 0 or c < 0 or
                r >= rows or c >= columns or
                board[r][c] == "#" or
                board[r][c] != word[i]
            ):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True

        return False