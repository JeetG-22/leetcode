class Solution(object):
    def removeElement(self, nums, val):
        #first
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        filtered_list = []
        for i in range(len(nums)):
            if(val == nums[i]):
                continue
            filtered_list.append(nums[i]) 
        nums[:len(filtered_list)] = filtered_list
        return len(filtered_list)