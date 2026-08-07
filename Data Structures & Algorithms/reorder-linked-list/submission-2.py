class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the list in-place: L0→L1→...→Ln  becomes  L0→Ln→L1→Ln-1→...
        Does this in O(n) time and O(1) extra space.
        """
        if not head or not head.next:
            return  # nothing to reorder for 0 or 1 node

        # ---------------------------------------------------------
        # STEP 1: Find the middle of the linked list
        # ---------------------------------------------------------
        # Using the "slow and fast pointer" technique:
        # - slow moves 1 node at a time
        # - fast moves 2 nodes at a time
        # When fast reaches the last node (or None), slow is at the middle.
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # At this point, 'slow' is the last node of the FIRST half.

        # ---------------------------------------------------------
        # STEP 2: Reverse the SECOND half of the list
        # ---------------------------------------------------------
        # 'second' starts right after the middle node.
        second = slow.next
        slow.next = None  # cut the list into two independent halves

        prev = None
        while second:
            tmp = second.next     # save the next node before we overwrite it
            second.next = prev    # reverse the pointer
            prev = second         # move prev forward
            second = tmp          # move second forward
        # 'prev' now points to the head of the reversed second half.

        # ---------------------------------------------------------
        # STEP 3: Merge the first half and reversed second half
        # ---------------------------------------------------------
        # first  -> head of first half  (e.g. 1 -> 2 -> 3)
        # second -> head of reversed second half (e.g. 5 -> 4)
        first, second = head, prev

        while second:
            # Save the "next" pointers of both halves before rewiring
            tmp1 = first.next
            tmp2 = second.next

            # Interleave: first -> second -> (rest of first half)
            first.next = second
            second.next = tmp1

            # Move both pointers forward to their saved next nodes
            first = tmp1
            second = tmp2
        # Loop naturally stops when 'second' becomes None
        # (the second half is always <= length of first half)