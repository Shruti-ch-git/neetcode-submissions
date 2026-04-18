from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a hashmap to store groups of anagrams
        hashmap = defaultdict(list)
        
        # Iterate through each string in the input list
        for s in strs:
            # Create a frequency count for the characters in the string
            count = [0] * 26  # Array of size 26 to store frequency of each letter
            
            # For each character in the string, increment the corresponding count
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Convert the count list to a tuple to be used as a hashmap key
            key = tuple(count)
            
            # Add the string to the hashmap using the character count as the key
            hashmap[key].append(s)
        
        # Return all the anagram groups as a list of lists
        return list(hashmap.values())
