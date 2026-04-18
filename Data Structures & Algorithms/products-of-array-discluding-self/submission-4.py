class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        s=[1]*l

        p=1
        for i in range(l):
            s[i]=p
            p*=nums[i]
        su=1
        for i in range(l-1, -1, -1):
            s[i]*=su
            su*=nums[i]
        return s 



                


        