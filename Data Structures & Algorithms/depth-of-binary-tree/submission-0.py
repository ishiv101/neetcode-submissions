# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #dfs use recursion
        def dfs(root: Node):
            if root is None: 
                return 0
            # go all the way down on the left side first and then all the way down on the right side
            return max(dfs(root.left), dfs(root.right)) + 1

        return dfs(root)

        
        