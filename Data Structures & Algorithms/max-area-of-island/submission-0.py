class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def bfs(start_row, start_col):
            area = 1
            q = deque()
            q.append((start_row, start_col))
            visited.add((start_row, start_col))

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for d_row, d_col in directions:
                    new_row = d_row + row
                    new_col = d_col + col
                    if (new_row in range(num_rows) and
                        new_col in range(num_cols) and
                        grid[new_row][new_col] == 1 and
                        (new_row, new_col) not in visited):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        area += 1

            return area

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = bfs(row, col)
                    max_area = max(max_area, area)

        return max_area