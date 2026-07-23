class MedianFinder:
    """
    We have a max heap representing the sorted left half of the stream, and a min heap representing the sorted right half of the stream.
    The tops of these heaps represent the middle of the stream so far.

    To get the median:
        - if len(left) == len(right): return (left[0] + right[0]) / 2
        - elif len(left) > len(right): return left[0]
        - else: return right[0]

    To add a number x:
        If x <= left[0], add to left. Else, add to right.
        If abs(len(left) - len(right)) > 1: rebalance heaps.

    To rebalance:
        Pop an element from the bigger heap and add it to the smaller heap.

    Adding a number: O(log n) time, as there could be at most 2 pushes and 1 pop (log n).
    Finding the median: O(1), since we just look at the 0th elements of the heaps.
    Space: O(n), since we store every element in the heaps.
    """

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                elt = heapq.heappop(self.left)
                heapq.heappush(self.right, -elt)
            elif len(self.left) < len(self.right):
                elt = heapq.heappop(self.right)
                heapq.heappush(self.left, -elt)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()