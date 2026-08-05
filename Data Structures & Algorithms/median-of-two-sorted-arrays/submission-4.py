class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a

        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a) - 1

        while True:
            # Partition index in a
            i = (l + r) // 2

            # Partition index in b so that
            # left side contains exactly 'half' elements
            j = half - i - 2

            # Elements around the partition
            aLeft = a[i] if i >= 0 else float("-inf")
            aRight = a[i + 1] if i + 1 < len(a) else float("inf")

            bLeft = b[j] if j >= 0 else float("-inf")
            bRight = b[j + 1] if j + 1 < len(b) else float("inf")

            # Valid partition:
            # every element on the left <= every element on the right
            if aLeft <= bRight and bLeft <= aRight:

                # Odd total length:
                # median is the first element on the right side
                if total % 2:
                    return min(aRight, bRight)

                # Even total length:
                # median is the average of the two middle values
                return (
                    max(aLeft, bLeft) +
                    min(aRight, bRight)
                ) / 2

            # Too many elements taken from a
            # Move partition left
            elif aLeft > bRight:
                r = i - 1

            # Need more elements from a
            # Move partition right
            else:
                l = i + 1