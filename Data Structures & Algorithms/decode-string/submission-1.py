class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                popped_values = []
                while stack and stack[-1] != "[":
                    popped_values.append(stack.pop())
                stack.pop()
                popped_values = popped_values[::-1]
                popped_value = "".join(popped_values)

                popped_nums = []
                while stack and stack[-1].isdigit():
                    popped_nums.append(stack.pop())
                popped_nums = popped_nums[::-1]
                popped_num = int("".join(popped_nums))
                
                stack.append(popped_num * popped_value)
            else:
                stack.append(c)

        return "".join(stack)