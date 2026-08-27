class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        n = len(nums)

        def dfs(i):
            if i >= n:
                res.append(sub.copy())
                return

            sub.append(nums[i])   # include nums[i]
            dfs(i + 1)

            sub.pop()             # undo

            dfs(i + 1)            # exclude nums[i]

        dfs(0)
        return res