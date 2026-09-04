from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        check=[(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                islands += 1
                grid[r][c] = "0"
                queue = deque([(r, c)])
                while queue:
                    row, col = queue.popleft()
                    for i,j in check:
                        nr = row + i
                        nc = col + j
                        if (
                            0 <= nr < rows and
                            0 <= nc < cols and
                            grid[nr][nc] == "1"
                        ):
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))

        return islands