class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row,col= len(grid), len(grid[0])
        n=0
        def dfs(i,j):
            if i>=row or j>=col or i<0 or j<0 or grid[i][j] == "0":
                return
            grid[i][j]='0'
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
        '''grid[i][j]= '1'
            return n'''
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    n += 1
                    dfs(r, c)

        return n

        