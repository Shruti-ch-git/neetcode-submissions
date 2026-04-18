class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[(p,q) for p,q in zip(position,speed)]
        pairs.sort(reverse=True)
        s=[]
        for i, j in pairs:
            t= (target-i)/j
            if s and s[-1]>=t:
                continue
            else:
                s.append(t)

        return len(s)
            
            

        