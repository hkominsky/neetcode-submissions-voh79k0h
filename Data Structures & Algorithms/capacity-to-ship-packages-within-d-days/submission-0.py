class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right

        def can_ship(capacity : int) -> bool:
            ships = 1
            curr_load = 0

            for weight in weights:
                if curr_load + weight > capacity:
                    ships += 1
                    curr_load = 0
                curr_load += weight

            return ships <= days

        while left <= right:
            mid = (left + right) // 2
            
            if can_ship(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

