"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Map from original node -> its copy.
        # Seeding with {None: None} means any pointer that is None
        # (e.g. tail.next or random pointing nowhere) maps cleanly to None,
        # avoiding a separate "if node else None" check later.
        old_to_copy = {None: None}

        # --- Pass 1: create a copy of every node (values only) ---
        # We don't wire up next/random yet because a node's random pointer
        # might point to a node we haven't created a copy for yet.
        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next

        # --- Pass 2: wire up next and random on the copies ---
        # By now every original node (and None) has an entry in the map,
        # so we can safely resolve pointers in any order.
        cur = head
        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]      # copy's next = copy of original's next
            copy.random = old_to_copy[cur.random]  # copy's random = copy of original's random
            cur = cur.next

        # Return the copy corresponding to the original head (None-safe).
        return old_to_copy[head]