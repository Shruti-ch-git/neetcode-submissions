class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        L=len(prerequisites)
        q=deque()
        graph=[ [] for _ in range(numCourses)]
        inorder= [0]*numCourses
        for course, req in  prerequisites:
            graph[req].append(course)
            inorder[course]+=1
        for i in range(numCourses):
            if inorder[i]==0:
                q.append(i)
        if not q:
            return False
        completed=0
        while q:
            course=q.popleft()
            completed+=1
            for i in graph[course]:
                inorder[i]-=1
                if inorder[i]==0:
                    q.append(i)
        return completed==numCourses
        