class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[0]*len(temperatures)
        out=[]
        for i,x in enumerate(temperatures):
            while out and x>out[-1][0]:
                a,b=out.pop()
                s[b]=i-b

            out.append((x,i))

        return(s)
                                

        