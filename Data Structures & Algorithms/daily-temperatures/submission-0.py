class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last_i = stack.pop()
                res[last_i] = i - last_i

            stack.append(i)
        
        return res