from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = [] # what is returned
        queue = deque([root]) # initialize the queue with the root node
        while len(queue) > 0: #while there are things in the queue repeat this
            n = len(queue) # tell how many node are in this level
            next_level = [] # new list that will be added to result
            for _ in range(n):
                node = queue.popleft() 
                next_level.append(node.val) # adds node value in level list
                for child in [node.left, node.right]: # adds nodes children to queue
                    if child is not None:
                        queue.append(child)
            result.append(next_level)

        
        return result
                

        