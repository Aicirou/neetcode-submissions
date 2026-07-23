# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # Initialize diameter as a list to modify it within the helper function
        self.diameter_value = 0
        self.diameter_helper(root)  # Call the helper function to compute diameter
        return self.diameter_value
    
    def diameter_helper(self, node):
        if not node:  # Exit condition: If the node is None, return 0
            return 0
        
        # Recursively find the depth of the left and right subtrees
        left_depth = self.diameter_helper(node.left)
        right_depth = self.diameter_helper(node.right)
        
        # Update the diameter value
        self.diameter_value = max(self.diameter_value, left_depth + right_depth)
        
        # Return the depth of the current node
        return max(left_depth, right_depth) + 1