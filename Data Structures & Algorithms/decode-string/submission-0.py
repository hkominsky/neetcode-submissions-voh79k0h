class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                popped_values = []
                mult_str = []

                while stack and stack[-1] != "[":
                    popped_values.append(stack.pop())
                
                stack.pop()
                popped_values = popped_values[::-1]
                popped_value = "".join(popped_values)

                while stack and stack[-1].isdigit():
                    mult_str.append(stack.pop())

                mult_str = mult_str[::-1]
                mult_str = "".join(mult_str)
                mult_num = int(mult_str)
                
                stack.append(mult_num * popped_value)
            else:
                stack.append(c)

        return "".join(stack)