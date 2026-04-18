from typing import List
from collections import defaultdict  # not used

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}  # normal dict

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)

        return list(hashmap.values())
