class Node:
    def __init__(self, key, val):
        """
        Initialize a doubly-linked list node to store key-value pairs.
        
        Args:
            key: The key for the cache entry
            val: The value associated with the key
        """
        self.key, self.val = key, val
        self.prev = self.next = None  # References to previous and next nodes in the linked list

class LRUCache:
    """
    Least Recently Used (LRU) Cache implementation using a hashmap and doubly-linked list.
    
    The hashmap provides O(1) lookups, while the doubly-linked list allows for O(1)
    insertions and removals to track usage order.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a specified capacity.
        
        Args:
            capacity: Maximum number of key-value pairs the cache can hold
        """
        self.cap = capacity                # Maximum capacity of the cache
        self.cache = {}                    # Hashmap for O(1) lookups: key -> node
        
        # Create dummy head (left) and tail (right) nodes for the doubly-linked list
        # This eliminates edge cases when inserting/removing from an empty list
        self.left, self.right = Node(0,0), Node(0,0)
        
        # Connect dummy nodes to form an empty doubly-linked list
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        """
        Remove a node from the doubly-linked list.
        
        Args:
            node: The node to remove from the list
        """
        # Extract references to adjacent nodes
        prev, nxt = node.prev, node.next
        
        # Update links to bypass the node being removed
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        """
        Insert a node at the right end (most recently used position) of the list.
        
        Args:
            node: The node to insert
        """
        # Get references to nodes that will be adjacent to the inserted node
        prev, nxt = self.right.prev, self.right
        
        # Update adjacent nodes to point to the new node
        prev.next = nxt.prev = node
        
        # Update the new node to point to its adjacent nodes
        node.next, node.prev = nxt, prev   

    def get(self, key: int) -> int:
        """
        Retrieve a value from the cache by key and mark it as recently used.
        
        Args:
            key: The key to look up
            
        Returns:
            The value associated with the key, or -1 if the key doesn't exist
        """
        if key not in self.cache:
            return -1  # Key not found
            
        # Mark as recently used by moving to the end of the list
        self.remove(self.cache[key])  # Remove from current position
        self.insert(self.cache[key])  # Insert at right end (most recently used)
        
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        """
        Add or update a key-value pair in the cache and mark it as recently used.
        If adding would exceed capacity, remove the least recently used item.
        
        Args:
            key: The key to add or update
            value: The value to associate with the key
        """
        # If key exists, remove the old node from the linked list
        if key in self.cache:
            self.remove(self.cache[key])
            
        # Create a new node and add it to both cache and linked list
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])  # Insert at right end (most recently used)

        # If we've exceeded capacity, remove the least recently used item
        # (the node after the left dummy node)
        if len(self.cache) > self.cap:
            lru = self.left.next  # Least recently used node
            self.remove(lru)      # Remove from linked list
            del self.cache[lru.key]  # Remove from hashmap