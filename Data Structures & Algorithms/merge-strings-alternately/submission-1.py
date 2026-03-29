class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = right = 0
        merged_words = []

        while left < len(word1) and right < len(word2):
            merged_words.append(word1[left])
            merged_words.append(word2[right])
            left += 1
            right += 1

        merged_words.append(word1[left:])
        merged_words.append(word2[right:])

        return "".join(merged_words)