class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in char_map:
                if not stack or stack.pop() != char_map[c]:
                    return False
            else:
                stack.append(c)

        return not stack