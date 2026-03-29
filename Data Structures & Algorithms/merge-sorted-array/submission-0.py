class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        write = m + n - 1

        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[write] = nums1[left]
                left -= 1
            else:
                nums1[write] = nums2[right]
                right -= 1
            write -= 1

        if right >= 0:
            nums1[:right + 1] = nums2[:right + 1]
            

        