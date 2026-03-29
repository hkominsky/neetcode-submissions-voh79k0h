class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        window_set = set()

        for right in range(len(s)):
            while s[right] in window_set:
                window_set.remove(s[left])
                left += 1

            window_set.add(s[right])
            max_length = max(max_length, len(window_set))

        return max_length