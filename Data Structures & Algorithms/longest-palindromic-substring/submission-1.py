class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []

        def check(l, r):
            # Check bounds before accessing s[l] and s[r]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            # l and r are now outside the palindrome
            palindrome = s[l + 1:r]

            res.append((len(palindrome), palindrome))

        for i in range(len(s)):
            check(i, i)       # Odd palindrome
            check(i, i + 1)   # Even palindrome

        res.sort(reverse=True)

        return res[0][1]