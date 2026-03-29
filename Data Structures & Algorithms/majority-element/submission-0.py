class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_counter = Counter(nums)

        return element_counter.most_common(1)[0][0]
