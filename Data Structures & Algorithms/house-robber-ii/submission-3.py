from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        @cache
        def dfs(i,nums):
            if i<0: 
                return 0 
            if i==0:
                return nums[0]

            # print("i:",i)
            # print("nums:",nums)
            return max(dfs(i-1,nums),nums[i]+dfs(i-2,nums))

        newnums0 = tuple(nums[:-1])
        newnums1 = tuple(nums[1:])
        return max(dfs(len(newnums0)-1,newnums0),dfs(len(newnums1)-1,newnums1))