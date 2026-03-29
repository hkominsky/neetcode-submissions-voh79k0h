class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevNums:
                return [prevNums[diff], index]
            prevNums[num] = index