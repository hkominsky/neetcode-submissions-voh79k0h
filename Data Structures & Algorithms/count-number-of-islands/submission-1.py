class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(start_row, start_col):
            q = deque()
            visited.add((start_row, start_col))
            q.append((start_row, start_col))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for d_row, d_col in directions:
                    new_row = d_row + row
                    new_col = d_col + col

                    if (new_row in range(num_rows) and
                        new_col in range(num_cols) and
                        (new_row, new_col) not in visited and
                        grid[new_row][new_col] == "1"):
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))

        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)

        return islands