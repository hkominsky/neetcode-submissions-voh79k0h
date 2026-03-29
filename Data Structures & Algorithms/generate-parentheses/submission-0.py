class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        m = n * 2

        def backtrack(path, open_count, closed_count):
            if len(path) == m:
                res.append("".join(path))

            if n > open_count:
                path.append("(")
                backtrack(path, open_count + 1, closed_count)
                path.pop()

            if open_count > closed_count:
                path.append(")")
                backtrack(path, open_count, closed_count + 1)
                path.pop()

        backtrack([], 0, 0)
        return res