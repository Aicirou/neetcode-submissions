class MedianFinder:

    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.s, self.l = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s, -1 * num)

        # make sure every num small is <= every num in large
        if (self.s and self.l and (-1 * self.s[0]) > self.l[0]):
            val = -1 * heapq.heappop(self.s)
            heapq.heappush(self.l, val)

        # uneven size?
        if len(self.s) > len(self.l):
            val = -1 * heapq.heappop(self.s)
            heapq.heappush(self.l, val)
        if len(self.l) > len(self.s):
            val = heapq.heappop(self.l)
            heapq.heappush(self.s, -1 * val)


    def findMedian(self) -> float:
        if len(self.s) > len(self.l):
            return -1 * self.s[0]
        if len(self.l) > len(self.s):
            return self.l[0]
        
        return (-1 * self.s[0] + self.l[0]) / 2
        
        