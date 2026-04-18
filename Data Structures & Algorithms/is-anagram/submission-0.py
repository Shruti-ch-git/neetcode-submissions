class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            left_half = merge_sort(left_half)
            right_half = merge_sort(right_half)
            return merge(left_half, right_half)

        def merge(left, right):
            merged = []
            left_index = 0
            right_index = 0
            # Merge the two sorted halves
            while left_index < len(left) and right_index < len(right):
                if left[left_index] <= right[right_index]:
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1

            # Add any remaining elements in left or right
            merged.extend(left[left_index:])
            merged.extend(right[right_index:])
            return merged

        # Use merge sort to sort both strings
        sorted_s = merge_sort(list(s))
        sorted_t = merge_sort(list(t))

        # Compare the sorted versions of both strings
        return sorted_s == sorted_t"""

        if len(s) != len(t):
            return False
        
        # Initialize two hash tables (dictionaries) to count the frequency of each character
        hash_table_s = {}
        hash_table_t = {}
        
        # Traverse both strings and populate the hash tables with character counts
        for i in range(len(s)):
            hash_table_s[s[i]] = hash_table_s.get(s[i], 0) + 1
            hash_table_t[t[i]] = hash_table_t.get(t[i], 0) + 1
        
        # Compare the two hash tables
        return hash_table_s == hash_table_t
