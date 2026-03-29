class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            
        curr.EndOfWord = True

    def search(self, word: str) -> bool:
        def search_from(node, word):
            curr = node

            for i in range(len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if search_from(child, word[i+1:]):
                            return True
                    return False
                elif word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]

            return curr.EndOfWord

        return search_from(self.root, word)
