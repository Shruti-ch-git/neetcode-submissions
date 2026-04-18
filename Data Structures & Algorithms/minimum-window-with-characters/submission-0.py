class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""

        l = 0
        h = {}
        w = {}

        for i in range(n):
            h[t[i]] = h.get(t[i], 0) + 1

        have, need = 0, len(h)
        res, resl = [-1, -1], float("infinity")

        for r in range(m):
            w[s[r]] = w.get(s[r], 0) + 1

            if s[r] in h and w[s[r]] == h[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resl:
                    res = [l, r]
                    resl = r - l + 1

                w[s[l]] -= 1
                if s[l] in h and w[s[l]] < h[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resl != float("infinity") else ""