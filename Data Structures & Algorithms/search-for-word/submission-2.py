class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        move=[(-1,0), (1,0), (0,1), (0,-1)]
        n=len(board)
        m=len(board[0])
        def dfs(row,col, letter):
            print(word[letter],row,col)
            if letter==len(word)-1:
                return True
            for r,c in move:
                newr= r+row
                newc= c+col
                if (0<=newr)and (newr<n) and(0<=newc) and (newc<m)and (board[newr][newc]== word[letter+1]):
                    temp=board[newr][newc]
                    board[newr][newc]="#"
                    if dfs(newr, newc, letter+1):
                        return True
                    board[newr][newc] = temp
            return False


        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    temp=board[i][j]
                    board[i][j]="#"
                    if dfs(i,j,0):
                        return True
                    board[i][j]=temp
                    
                    
        return False


        