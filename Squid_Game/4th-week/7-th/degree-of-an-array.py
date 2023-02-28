class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dicts = defaultdict(list)
        for i, n in enumerate(nums):
            dicts[n].append(i)        
        degree = max([len(x) for x in dicts.values()])
        
        ans = len(nums)
        for idx in dicts.values():
            if len(idx) == degree:
                ans = min(ans, idx[-1] - idx[0])
        return ans + 1  