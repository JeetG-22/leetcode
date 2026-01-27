import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2
            val = self.find_min(piles, h, mid)
            if val < 0:
                low = mid + 1
            else:
                high = mid - 1
        return low


        
    def find_min(self, piles, h, k):
        dur = 0
        for banana in piles:
            dur += math.ceil(banana / k)
        if dur > h:
            return -1
        else:
            return 1
        