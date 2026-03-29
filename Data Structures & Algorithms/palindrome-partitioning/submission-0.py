class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(index, path):
            if index == len(s):
                res.append(path[:])
                return

            for i in range(index, len(s)):
                sub = s[index:i + 1]

                if isPalindrome(sub):
                    path.append(sub)
                    backtrack(i + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res