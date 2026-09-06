class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=len(prerequisites)
        q=deque()
        l=[]
        inorder= [0]*numCourses
        graph =[[] for _ in range(numCourses)] 
        for course, prereq in prerequisites:
            inorder[course]+=1
            graph[prereq].append(course)
        for course in range(numCourses):
            if inorder[course]==0:
                q.append(course)
        completed=0
        while q:
            new= q.popleft()
            l.append(new)
            completed+=1
            for n in graph[new]:
                inorder[n]-=1
                if inorder[n]==0:
                    q.append(n)
        return l if completed==numCourses else []





        