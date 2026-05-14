class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for i in nums:
            h[i] = h.get(i, 0) + 1

        return sorted(h, key=h.get, reverse=True)[:k]