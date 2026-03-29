class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [(-((point[0]**2 + point[1]**2) ** 0.5) , point) for point in points]
        heapq.heapify(max_heap)

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        return [heapq.heappop(max_heap)[1] for _ in range(len(max_heap))]