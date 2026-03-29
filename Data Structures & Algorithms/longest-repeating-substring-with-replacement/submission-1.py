class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        max_length = 0
        left = 0

        for right in range(len(s)):
            chars[s[right]] += 1

            max_char = max(chars.values())
            curr_len = right - left + 1
            if curr_len - max_char > k:
                chars[s[left]] -= 1
                left += 1
                
            max_length = max(max_length, right - left + 1)

        return max_length