# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Convert tree to string using preorder traversal"""
        result = []  # List to collect node values in preorder
        
        def preorder(node):
            if not node:
                result.append("null")         # Mark empty positions with "null"
            else:
                result.append(str(node.val))  # Convert node value to string
                preorder(node.left)           # Recursively serialize left subtree
                preorder(node.right)          # Recursively serialize right subtree
        
        preorder(root)
        print(result)  # Debug: shows the preorder sequence
        return ",".join(result)  # Convert list to comma-separated string

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Convert string back to tree using preorder reconstruction"""
        values = data.split(",")  # Split string back into list of values
        self.index = 0            # Track current position in values array
        
        def build():
            # Get current value and advance index
            val = values[self.index]
            self.index += 1
            
            # Base case: null node
            if val == "null":
                return None
            
            # Create node with current value
            node = TreeNode(int(val))
            # Recursively build left subtree (preorder: left comes next)
            node.left = build()
            # Recursively build right subtree (preorder: right comes after left)
            node.right = build()
            
            return node
        
        return build()