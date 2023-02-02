class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sums = 0
        steps = 0
        heapq.heapify(nums)
        while nums:
            num = heapq.heappop(nums)
            sums += num
            if num > sums:
                sums = num
                steps += 1
                
        return steps

            
