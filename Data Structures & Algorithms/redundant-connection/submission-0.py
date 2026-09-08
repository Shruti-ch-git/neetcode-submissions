class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        adj = [[] for _ in range(n+1)]
        visited= [False]*(n+1)
        result=[]
        cycle=set()
        cyclestart=-1
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node, parent):
            nonlocal cyclestart
            if visited[node]:
                cyclestart = node
                return True
            visited[node]= True
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if dfs(neighbour, node):
                    if cyclestart != -1:
                        cycle.add(node)
                    if node== cyclestart:
                        cyclestart=-1
                    return True
            return False
        dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return[u,v]

        return []
            
        