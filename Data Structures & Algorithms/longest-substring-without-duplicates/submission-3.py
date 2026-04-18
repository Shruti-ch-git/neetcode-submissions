class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        ml =0
        p=set()
        while r<len(s):
            if s[r] not in p:
                p.add(s[r])
                ml = max(r-l+1 , ml)
                r+=1
            else:
                p.remove(s[l])
                l=l+1

        return ml

        