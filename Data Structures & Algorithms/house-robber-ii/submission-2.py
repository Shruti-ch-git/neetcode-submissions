class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def r(house):
            prev1=0
            prev2=0
            for i in house:
                curr= max(prev1, prev2+i)
                print(curr)
                prev2=prev1
                prev1= curr
            return prev1
        nofirst= r(nums[1:])
        nolast=r(nums[:-1])
        return max(nofirst, nolast)
            


        