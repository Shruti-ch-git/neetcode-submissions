class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        max_freq = max(freqs.values())
        num_max = 0
        for freq in freqs:
            if freqs[freq] == max_freq:
                num_max += 1
        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max)