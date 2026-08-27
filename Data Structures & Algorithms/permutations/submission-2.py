class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm=[[]]
        for n in nums:
            new=[]
            for p in perm:
                for i in range(len(p)+1):
                    p_copy=p.copy()
                    p_copy.insert(i,n)
                    new.append(p_copy)
            perm=new
        return perm
                
                    
                    
                    
            
        