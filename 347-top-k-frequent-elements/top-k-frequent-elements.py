import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        heap = []
        for key in counts.keys():
            heapq.heappush(heap, (counts[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = [] 
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        