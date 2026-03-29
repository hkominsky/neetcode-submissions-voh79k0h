# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, high):
            count = 0

            if not node:
                return 0

            if node.val >= high:
                count += 1

            new_high = max(high, node.val)

            count += dfs(node.left, new_high)
            count += dfs(node.right, new_high)

            return count

        return dfs(root, root.val)