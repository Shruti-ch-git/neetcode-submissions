class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]  # Bucket size from 0 to n
        
        # Step 3: Place each number in the corresponding bucket based on its frequency
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # Step 4: Collect the top k frequent elements from the buckets
        result = []
        for i in range(n, 0, -1):  # Start from the highest frequency bucket
            if buckets[i]:
                result.extend(buckets[i])  # Add all elements in this bucket
                if len(result) >= k:
                    break
        
        # Return the first k elements
        return result[:k]