# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Approach 1: DFS with min/max bounds
        Time: O(n), Space: O(h) where h is height
        """
        def validate(node, min_val, max_val):
            # Empty node is valid
            if not node:
                return True
            
            # Check if current node violates BST property
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate subtrees with updated bounds
            # Left subtree: all values must be < node.val
            # Right subtree: all values must be > node.val
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        # Start with infinite bounds
        return validate(root, float('-inf'), float('inf'))