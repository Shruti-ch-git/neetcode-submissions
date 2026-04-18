class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        h = {}
        w = {}

        for ch in s1:
            h[ch] = h.get(ch, 0) + 1

        for i in range(m):
            w[s2[i]] = w.get(s2[i], 0) + 1

        if w == h:
            return True

        l = 0
        for r in range(m,n):
            w[s2[r]] = w.get(s2[r],0)+1
            w[s2[l]]-=1
            if w[s2[l]]==0:
                del w[s2[l]]
            if w==h:
                return True
            l+=1
                          

        return False
"""
        m,n=len(s1), len(s2)
        if m>n:
            return False
        h={}
        w={}
        l=0
        for i in range(m):
            h[s1[i]]=h.get(s1[i],0)+1
        need= sum(h.values())
        for i in range(n):
            w[s2[i]]=w.get(s2[i],0)+1
            if s2[i] in h and h[s2[i]] >0:
                need-=1
                h[s2[i]]-=1
            if need ==0:
                return True
        return False
"""





        
        