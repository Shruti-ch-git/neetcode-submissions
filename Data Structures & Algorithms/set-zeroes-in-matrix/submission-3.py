class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        q=deque()

        def dfs(i,j):
            for r in range(row):
                matrix[r][j]=0

            for c in range(col):
                matrix[i][c]=0

        for i in range(row):
            for j in range(col):
                if matrix[i][j]== 0:
                    q.append((i,j))
        while q:
            rnew, cnew=q.popleft()
            dfs(rnew, cnew)

        
        
        