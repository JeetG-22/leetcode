import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x,y = point
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (dist, point))
        res = []
        k_closest = heapq.nsmallest(k, heap)
        for dist, point in k_closest:
            res.append(point)
        return res
            
        