# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Count good nodes in binary tree.
        A node is good if its value >= max value on path from root to that node.
        """
        if not root:
            return 0
        
        def dfs(node, path_max):
            if not node:
                return 0
            
            # Count current node if it's good (>= path maximum)
            good_count = 1 if node.val >= path_max else 0
            
            # Update path maximum for children
            new_max = max(path_max, node.val)
            
            # Recursively count good nodes in subtrees
            good_count += dfs(node.left, new_max)
            good_count += dfs(node.right, new_max)
            
            return good_count
        
        return dfs(root, root.val)      