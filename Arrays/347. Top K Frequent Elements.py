class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minheap = []
        for num, count in freq.items():
            print((count, num))
            heapq.heappush(minheap, (count, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        while minheap:
            res.append(heapq.heappop(minheap)[1])
        return res