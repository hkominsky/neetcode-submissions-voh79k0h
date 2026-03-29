class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, total, path):
            if total > target or index >= len(nums):
                return

            if total == target:
                res.append(path[:])
                return

            path.append(nums[index])
            backtrack(index, total + nums[index], path)
            path.pop()

            backtrack(index + 1, total, path)

        backtrack(0, 0, [])
        return res