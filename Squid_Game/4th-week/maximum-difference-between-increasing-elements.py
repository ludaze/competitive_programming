class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if not nums or len(nums) ==1:
            return -1
        maxdiff = -1
        maxim = [0 for i in range(len(nums)+1)]
        for k in range(len(nums)-1,-1,-1):
            maxim[k] = max(maxim[k+1],nums[k])
        for j in range(len(nums)):
            if nums[j]<maxim[j]:
                maxdiff = max(maxdiff,maxim[j]-nums[j])
        return maxdiff