class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        l=1
        m=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i]-nums[i-1]==1:
                l+=1
            else:
                m=max(l,m)
                l=1
        return max(m,l)


        