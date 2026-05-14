from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord('a')]+=1
            k=tuple(count)
            if k not in h:
                h[k]=[]
            h[k].append(i)
        return list(h.values())

                
        