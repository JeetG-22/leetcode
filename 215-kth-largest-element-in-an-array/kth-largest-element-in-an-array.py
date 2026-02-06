import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [num * -1 for num in nums]
        heapq.heapify(nums)

        k -= 1
        while k:
            heapq.heappop(nums)
            k -= 1
        return -heapq.heappop(nums)
        