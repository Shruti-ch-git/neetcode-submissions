class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Initialize the output array for the result
        output = [1] * n
        
        # Step 2: Calculate the prefix products and store them in the output array
        prefix_product = 1
        for i in range(n):
            output[i] = prefix_product
            prefix_product *= nums[i]
        
        # Step 3: Calculate the suffix products and update the output array
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]
        
        return output
