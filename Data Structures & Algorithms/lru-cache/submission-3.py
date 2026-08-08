"""
An LRU (Least Recently Used) Cache is a memory-management system that discards the item used longest ago when the cache reaches its maximum capacity.
To achieve $O(1)$ time complexity (constant time) for both retrieving values (get) and adding/updating values (put), 
this solution uses a combination of two data structures:
Hash Map (self.cache): Stores key -> Node mappings. This allows $O(1)$ direct access to any node in memory without searching through the list.
Doubly-Linked List: Tracks the order of item usage.
self.left (Dummy Head): The node immediately after self.left (self.left.next) is always the Least Recently Used (LRU) item.
self.right (Dummy Tail): The node immediately before self.right (self.right.prev) is always the Most Recently Used (MRU) item.
"""
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # Dummy nodes for list boundaries
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        """Remove node from doubly-linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Node) -> None:
        """Insert node at the MRU position (right before self.right)."""
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        """Retrieve value and mark node as Most Recently Used."""
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """Add/update key-value pair and evict LRU node if capacity is exceeded."""
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.cap:
            # Evict LRU node (node after dummy left)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
