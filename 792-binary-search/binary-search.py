class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, 0, len(nums) - 1, target)

    def bin_search(self, nums, l, h, target):
        mid = (h+l) // 2
        if nums[mid] == target:
            return mid
        if l > h:
            return -1
        
        if nums[mid] < target:
            return self.bin_search(nums, mid + 1, h, target)
        else:
            return self.bin_search(nums,l, mid - 1, target)

        