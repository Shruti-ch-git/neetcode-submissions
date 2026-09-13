class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=0
        beforeprev=0
        for money in nums:
            curr= max(prev, beforeprev+money)
            beforeprev= prev
            prev= curr
        return prev

            



        