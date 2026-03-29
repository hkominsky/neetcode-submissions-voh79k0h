class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in prevNums:
                return [prevNums[complement], i]
            prevNums[n] = i
            
        return