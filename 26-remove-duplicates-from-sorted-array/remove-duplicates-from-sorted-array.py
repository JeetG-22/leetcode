class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unq_set = sorted(set(nums))
        nums[:len(unq_set)] = unq_set
        return len(unq_set)