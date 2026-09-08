class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        visited= [False]*n
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)# dict list is formed with all the possible edges
            '''
            0=1
            1=0,2
            2=1
            3=4
            4=3
            '''
        def dfs(node):
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour]= True
                    dfs(neighbour)
        components=0
        for node in range(n):
            if not visited[node]:
                visited[node]= True
                components+=1
                dfs(node)


        return components


            

