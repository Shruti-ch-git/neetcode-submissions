class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        fresh, time=0,0
        row, col= len(grid), len(grid[0]) 
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        d=[[0,1], [-1,0], [0,-1], [1,0]]
        while fresh and q:
            l= len(q)
            for i in range(l):
                a,b=q.popleft()

                for ad,ab in d:
                    k,l= a+ad, b+ab
                    if ((k in range(row) and (l in range(col) and grid[k][l]==1))):
                        grid[k][l]=2
                        q.append((k,l))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
        
                    
                        
                        
                        


                    
                    
                    
                    
                    
                    
                    
                
            
        