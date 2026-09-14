class CountSquares:
    def __init__(self):
        self.h=defaultdict(int)
        self.pt=[]
        

    def add(self, point: List[int]) -> None:
        self.h[tuple(point)]+=1 #python list cannot be hash key
        self.pt.append(point)


    def count(self, point: List[int]) -> int:
        res=0
        px,py=point
        for x,y in self.pt:
            if (abs(py-y))!= (abs(px-x)) or x==px or y==py:
                continue
            res+= self.h[(x,py)]* self.h[px,y]
        return res
            
            
            


        
