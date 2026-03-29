class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem_counter = Counter(nums)

        return elem_counter.most_common(1)[0][0]
