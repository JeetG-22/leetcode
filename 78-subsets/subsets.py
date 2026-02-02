class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #choice to append that element to the list
            subset.append(nums[i])
            dfs(i+1)

            #choice to not append it
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
        