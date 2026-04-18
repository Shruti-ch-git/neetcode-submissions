class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1=len(nums)
        n=set(nums)
        l2=len(n)
        if l1>l2:
            return True
        else:
            return False
