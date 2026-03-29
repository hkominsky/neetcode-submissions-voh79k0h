class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for index, num in enumerate(nums):
            if num in last_seen:
                if index - last_seen[num] <= k:
                    return True

            last_seen[num] = index

        return False