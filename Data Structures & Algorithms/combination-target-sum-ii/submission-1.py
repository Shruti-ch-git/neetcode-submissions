class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        n=len(candidates)
        def dfs(i, curr, total):
            if total==target:
                res.append(curr.copy())
                return
            if total>target or i==n:
                return
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()
            while i+1<n and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1, curr , total)
        dfs(0,[],0)
        return res
            
        