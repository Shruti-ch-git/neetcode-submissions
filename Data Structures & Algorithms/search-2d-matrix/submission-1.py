class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c= len(matrix), len(matrix[0])
        x,y=0,r*c-1
        
        while x <= y:
            mid=(x+y)//2
            p,q= mid//c, mid%c

            if matrix[p][q] == target:
                return True
            elif matrix[p][q]>target:
                y=mid-1
            else:
                x=mid+1
        return False
            
            

        