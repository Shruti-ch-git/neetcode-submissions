class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r,c= len(grid), len(grid[0])
        m=0
        check=[[0,1], [0,-1], [1,0], [-1,0]]
        d=deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j]!=1:
                    continue
                n=1
                grid[i][j]=0
                d.append((i,j))
                while d:
                    p,q=d.popleft()
                    for ll,rr in check:
                        new_r = p + ll  # Change 2: use p, not i
                        new_c = q + rr
                        if (0 <= new_r < r and 0 <= new_c < c and
                            grid[new_r][new_c] == 1):
                            n+=1
                            grid[new_r][new_c]=0
                            d.append((new_r, new_c))
                m=max(m,n)

        return m
            



        