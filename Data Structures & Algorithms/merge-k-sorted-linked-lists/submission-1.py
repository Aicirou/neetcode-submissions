# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge cases: if the input is empty or null, return null
        if not lists or len(lists) == 0:
            return None
        
        # Continue until we're left with just one list (the final merged list)
        # This is the divide and conquer approach that gives us O(log k) complexity
        while len(lists) > 1:
            mergedLists = []  # Temporary array to store merged pairs

            # Process lists in pairs (i, i+1)
            # The step of 2 means we're pairing adjacent lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # First list in the pair
                l2 = lists[i+1] if (i+1) < len(lists) else None  # Second list or None if odd number of lists
                
                # Merge the pair and add to our new list
                # This is where we're applying the divide-and-conquer strategy
                mergedLists.append(self.mergeList(l1, l2))
            
            # Replace our original list array with the new array of merged pairs
            # This reduces the number of lists by roughly half in each iteration
            lists = mergedLists
        
        # After the while loop, only one list remains, which is our answer
        return lists[0]

    def mergeList(self, l1, l2):
        # Standard merge procedure for two sorted linked lists - O(n) time complexity
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        tail = dummy  # Pointer to build the result list

        # Compare nodes from both lists and add smaller value to result
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # If one list is exhausted, attach the remainder of the other list
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        # Return the merged list (excluding the dummy node)
        return dummy.next

# Time Complexity Analysis:
# - The merge operation (mergeList) for two lists takes O(n) time where n is total nodes
# - We're doing log k iterations of the main while loop (as we halve the number of lists each time)
# - In each iteration, we process all n nodes across all lists
# - Therefore, the overall time complexity is O(n log k) where:
#   - n is the total number of nodes across all lists
#   - k is the number of linked lists
# 
# Space Complexity: O(1) extra space (not counting the output)