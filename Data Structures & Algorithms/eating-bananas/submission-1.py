class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        x,y=1,max(piles)
        a=y
        while x<=y:
            m=(x+y)//2
            h1=0
            for i in piles:
                h1 +=(i+m-1)//m
            if h1<= h:
                a=m
                y=m-1
            else:
                x=m+1
        return a

        

        