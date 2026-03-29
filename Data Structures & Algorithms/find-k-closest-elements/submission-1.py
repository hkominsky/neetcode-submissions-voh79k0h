class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = k

        while right < len(arr) and x - arr[left] > arr[right] - x:
            left += 1
            right += 1
        
        return arr[left:right]