from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False  # Cycle found

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Don't go directly back

                if not dfs(neighbor, node):
                    return False

            return True

        # No cycle and every node must be connected
        return dfs(0, -1) and len(visited) == n
        