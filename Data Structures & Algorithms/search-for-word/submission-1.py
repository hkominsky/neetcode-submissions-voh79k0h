class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def backtrack(i, j, index):
            if index == len(word):
                return True

            if (i < 0 or i >= n or j < 0 or j >= m or
                word[index] != board[i][j] or board[i][j] == '!'):
                return False

            temp = board[i][j]
            board[i][j] = '!'

            for di, dj in directions:
                if backtrack(i + di, j + dj, index + 1):
                    board[i][j] = temp
                    return True

            board[i][j] = temp
            return False

        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True

        return False