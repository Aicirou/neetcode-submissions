# ============================================================
# Solution 1: Sorting
# Time: O(n logn)
# Space: O(n)
# ============================================================

class Solution_Sorting:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        arr = []
        for num, count in freq.items():
            arr.append([count, num])
        
        arr.sort()

        res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        for group in arr[-k:]:
            res.append(group[1])
        return res


# ============================================================
# Solution 2: Min Heap
# Time: O(n log k)
# Space: O(n + k)
# Where n is the length of the array and k is the number of top frequent elements.
# ============================================================

class Solution_MinHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)  
        
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


# ============================================================
# Solution 2: Bucket Sort
# Time: O(n)
# Space: O(n)
# ============================================================

class Solution_BucketSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

Solution = Solution_BucketSort

