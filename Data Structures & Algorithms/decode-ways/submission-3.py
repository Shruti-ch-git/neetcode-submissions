#wow
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            #126= 1111 ; 120= 0001 ; 102=0011

            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"):
            # Example: s = "126"
            #
            # Start: dp[3] = 1
            #
            # i = 2, "6":
            # dp[2] = dp[3] = 1
            # DP: [?, ?, 1, 1]
            #
            # i = 1, "2":
            # One digit:  dp[1] = dp[2] = 1
            # Two digits: "26" is valid, add dp[3] = 1
            # dp[1] = 1 + 1 = 2
            # DP: [?, 2, 1, 1]
            #
            # i = 0, "1":
            # One digit:  dp[0] = dp[1] = 2
            # Two digits: "12" is valid, add dp[2] = 1
            # dp[0] = 2 + 1 = 3
            # Final DP: [3, 2, 1, 1]
            #
            # Decodings: 1|2|6, 1|26, 12|6

                dp[i] += dp[i + 2]
        return dp[0]