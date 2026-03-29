class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1

            length = int(s[left:right])
            left = right + 1

            res.append(s[left:left+length])
            left += length

        return res