# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Convert tree to string using preorder traversal"""
        result = []
        
        def preorder(node):
            if not node:
                result.append("null")  # Mark empty spots
            else:
                result.append(str(node.val))  # Add the value
                preorder(node.left)           # Go left
                preorder(node.right)          # Go right
        
        preorder(root)
        print(result)
        return ",".join(result)  # Join with commas

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.index = 0

        def build():
            val = values[self.index]
            self.index += 1

            if val == "null":
                return None
            
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            
            return node
        
        return build() 



