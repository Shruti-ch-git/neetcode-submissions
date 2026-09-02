class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #iteration
        res=[[]]
        for i in range(len(nums)):
            res+= [sub + [nums[i]] for sub in res]
        return res        