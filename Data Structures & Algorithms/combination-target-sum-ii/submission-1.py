class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, path):
            if sum(path) == target:
                res.append(path[:])

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if sum(path) + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res