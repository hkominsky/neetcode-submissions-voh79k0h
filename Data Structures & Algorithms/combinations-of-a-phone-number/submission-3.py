class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        combinations = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",           
        }

        def backtrack(index, path):
            if not digits:
                return []
                
            if index == len(digits):
                res.append("".join(path))
                return

            digit = digits[index]
            for combo in combinations[digit]:
                path.append(combo)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res