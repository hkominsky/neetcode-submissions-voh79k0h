# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        def dfs(root):
            if not root:
                return None

            vals.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        sorted_vals = sorted(vals)
        return sorted_vals[k-1]


