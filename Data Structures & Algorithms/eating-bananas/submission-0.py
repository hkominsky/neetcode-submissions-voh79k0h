class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        def can_eat(k: int) -> bool:
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
            return total_hours <= h

        while left <= right:
            mid = (left + right) // 2

            if can_eat(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return res