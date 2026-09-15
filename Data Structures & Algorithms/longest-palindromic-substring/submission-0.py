class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def check(l, r):
            nonlocal res

            # Bounds must be checked before accessing s[l] and s[r]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            # l and r are now one position outside the palindrome
            palindrome = s[l + 1:r]

            if len(palindrome) > len(res):
                res = palindrome

        for i in range(len(s)):
            check(i, i)       # Odd-length palindrome
            check(i, i + 1)   # Even-length palindrome

        return res