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
        i =  0
        while i < k:
            res.append(heapq.heappop(heap)[1]) 
            i += 1
        return res
            
        