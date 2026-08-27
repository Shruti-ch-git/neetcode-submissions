class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n= len(nums)
        sub=[]
        s=[]
        def dfs(i, total):
            if total==target:
                s.append(sub.copy())
                return
            if total>target or i>=len(nums):
                return 
            sub.append(nums[i])
            dfs(i, total+nums[i])
            sub.pop()
            dfs(i+1, total )
        dfs(0, 0)
        return s

        