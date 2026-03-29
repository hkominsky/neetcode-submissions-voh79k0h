class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(i, j):
            q = deque()
            visited.add((i, j))
            q.append((i, j))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for direction_row, direction_col in directions:
                    r, c = row + direction_row, col + direction_col
                    if ((r) in range(rows) and
                        (c) in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for i in range(rows):
            for j in range(cols):
                pos = grid[i][j]
                if pos == "1" and (i, j) not in visited:
                    bfs(i, j)
                    count += 1

        return count
                