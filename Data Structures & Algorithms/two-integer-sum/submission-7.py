class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in prev_nums:
                return [prev_nums[diff], index]

            prev_nums[num] = index