class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        INF = 2147483647

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                new_i = i + di
                new_j = j + dj

                if new_i in range(n) and new_j in range(m) and grid[new_i][new_j] == INF:
                    grid[new_i][new_j] = grid[i][j] + 1
                    q.append((new_i, new_j))