# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        if not head:
            return
    
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
    
        if len(nodes) <= 2:  # Handle edge cases with short lists
            return
    
        reordered_nodes = []
        left, right = 0, len(nodes) - 1
        while left < right:  # Ensures correct handling of odd number of nodes
            reordered_nodes.append(nodes[left])
            left += 1
            reordered_nodes.append(nodes[right])
            right -= 1
    
        if left == right:  # Append the middle element for odd number of nodes
            reordered_nodes.append(nodes[left])
    
        # Reconnect the nodes (modify the existing linked list)
        curr = head
        for i in range(len(reordered_nodes)):
            curr.val = reordered_nodes[i].val  # Modify the values directly
            if i < len(reordered_nodes) - 1:
                curr.next = reordered_nodes[i + 1]
            else:
                curr.next = None  # Set the last node's next to None
            curr = curr.next