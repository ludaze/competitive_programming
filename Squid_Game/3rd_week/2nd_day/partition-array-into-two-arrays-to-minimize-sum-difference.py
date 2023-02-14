class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 2 
        def get_sums(nums): 
            res = {}
            N = len(nums)
            for k in range(1, N+1): 
                sums = []
                for comb in combinations(nums, k):
                    s = sum(comb)
                    sums.append(s)
                res[k] = sums
            return res
        
        left, right = nums[:N], nums[N:]
        left_sums, right_sums = get_sums(left), get_sums(right)
        res = abs(sum(left) - sum(right))
        total = sum(nums) 
        half = total // 2
        for k in range(1, N):
            lefts = left_sums[k] 
            rights = right_sums[N-k] 
            rights.sort()
            for x in lefts:
                r = half - x 
                p = bisect.bisect_left(rights, r) 
                for q in [p, p-1]:
                    if 0 <= q < len(rights):
                        left_ans_sum = x + rights[q]
                        right_ans_sum = total - left_ans_sum
                        diff = abs(left_ans_sum - right_ans_sum)
                        res = min(res, diff) 
        return res