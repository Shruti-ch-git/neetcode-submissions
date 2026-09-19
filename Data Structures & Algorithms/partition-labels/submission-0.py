class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        # Store the last occurrence of every character
        for i in range(len(s)):
            last[s[i]] = i

        output = []
        l = 0
        r = 0

        for i in range(len(s)):
            # Current partition must include the last occurrence
            # of every character encountered
            r = max(r, last[s[i]])

            # We reached the end of the current partition
            if i == r:
                output.append(r - l + 1)
                l = i + 1

        return output