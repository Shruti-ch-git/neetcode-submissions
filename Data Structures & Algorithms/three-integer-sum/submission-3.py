class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=set()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    sum= nums[i]+nums[j] +nums[k]
                    if sum==0:
                        triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                        s.add(triplet)
        return [list(x) for x in s]
                        
        