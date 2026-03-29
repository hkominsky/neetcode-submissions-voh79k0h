class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.heap = nums
        self.remove()

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.remove()
        return self.heap[0]
        
    def remove(self):
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
