class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(s2 - s1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(int(s2 / s1))
            else:
                stack.append(int(token))

        return stack[0]