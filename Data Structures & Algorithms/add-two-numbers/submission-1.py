# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node simplifies edge cases (no need to special-case the head of result list)
        dummy = ListNode()
        cur = dummy       # pointer used to build the result list
        carry = 0         # carry-over from addition (0 or 1)

        # Keep looping while there are digits left in either list, or a carry remains
        while l1 or l2 or carry:
            # If one list is shorter/exhausted, treat its missing digit as 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Add digits plus carry from previous step
            add = v1 + v2 + carry
            carry = add // 10   # new carry for next iteration
            val = add % 10      # digit to store in this node

            # Attach new node with the computed digit
            cur.next = ListNode(val)

            # Advance all pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # dummy.next is the actual head of the result (dummy itself holds no real data)
        return dummy.next