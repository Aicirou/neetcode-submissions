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
        
        stack = [root]
        depth_map = {}
        diameter = 0

        while stack:
            node = stack[-1]

            # check if both childrens are visited or not null
            if node.left in depth_map or not node.left:
                if node.right in depth_map or not node.right:
                    #pop the node and calculate its depth
                    stack.pop()

                    left_depth = depth_map.get(node.left, 0)
                    right_depth = depth_map.get(node.right, 0)

                    diameter = max(diameter, left_depth + right_depth)

                    depth_map[node] = max(left_depth, right_depth) + 1
                else:
                    stack.append(node.right)
            else:
                stack.append(node.left)
        return diameter