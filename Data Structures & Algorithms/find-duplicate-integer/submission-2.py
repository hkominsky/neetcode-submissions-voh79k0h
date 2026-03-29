class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            count = sum(n <= mid for n in nums)

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left