class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Convert the list to a set for O(1) lookups
        num_set = set(nums)
        
        # Step 2: Initialize a variable to track the longest sequence length
        longest = 0
        
        # Step 3: Iterate through each number in the set
        for num in num_set:
            # Step 4: Check if 'num' is the start of a sequence
            if num - 1 not in num_set:  # This means `num` is the start of a sequence
                current_num = num
                current_streak = 1
                
                # Step 5: Count the length of the consecutive sequence starting from `num`
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Step 6: Update the longest sequence found
                longest = max(longest, current_streak)
        
        return longest
