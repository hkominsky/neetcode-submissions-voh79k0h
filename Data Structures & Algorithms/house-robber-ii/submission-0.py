class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_helper(nums):
            memo = [-1] * len(nums)

            def dfs(i):
                if i < 0 or i >= len(nums):
                    return 0
                if memo[i] != -1:
                    return memo[i]

                memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
                return memo[i]

            return dfs(0)

        with_first = rob_helper(nums[:-1])
        without_first = rob_helper(nums[1:])

        return max(with_first, without_first)