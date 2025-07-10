class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return 2 * nums
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums