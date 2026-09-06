class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        l= len(prerequisites)
        q=deque()

        graph =[[] for _ in range(numCourses)]
        indegree= [0]* numCourses
        for course, req in prerequisites:
            graph[req].append(course)
            indegree[course]+=1
        for course in range(numCourses):
            if indegree[course]==0:
                q.append(course)
        completed=0
        while q:
            course= q.popleft()
            completed+=1
            for n in graph[course]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)

        return completed==numCourses
            


        


