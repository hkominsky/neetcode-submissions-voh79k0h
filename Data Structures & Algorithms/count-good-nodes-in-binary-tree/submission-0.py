# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, high):
            nonlocal count

            if not node:
                return 0

            if node.val >= high:
                count += 1

            new_high = max(high, node.val)

            dfs(node.left, new_high)
            dfs(node.right, new_high)

            return count

        return dfs(root, root.val)