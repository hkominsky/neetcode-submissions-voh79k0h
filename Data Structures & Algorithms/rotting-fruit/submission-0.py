class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    new_i = i + di
                    new_j = j + dj
                    if new_i in range(n) and new_j in range(m) and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        q.append((new_i, new_j))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1
