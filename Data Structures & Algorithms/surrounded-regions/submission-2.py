class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 
        row, col= len(board), len(board[0])
        move=[[0,1], [1,0], [-1, 0], [0,-1]]
        q=deque()
        def add(r,c):
            if board[r][c]=="O":
                board[r][c]="T"
                q.append((r,c))
        for c in range(col):
            add(0,c)
            add(row-1, c)
        for c in range(row):
            add(c, 0)
            add(c, col-1)
        while q:
            r,c=q.popleft()
            for i,j in move:
                newr=r+i
                newc= c+j
                if (0<= newr< row and 0<=newc< col and board[newr][newc]=="O"):
                    board[newr][newc]="T"
                    q.append((newr, newc))
        for i in range(row):
            for j in range(col):
                if board[i][j]=="T":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"
                    


        



        