class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        a = 0

        for i, h in enumerate(heights):
            start = i
            while s and s[-1][1] > h:
                p, q = s.pop()
                a = max(a, q * (i - p))
                start = p
            s.append((start, h))

        for p, q in s:
            a = max(a, q * (len(heights) - p))

        return a