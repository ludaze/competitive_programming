class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        
        for i in set(nums):
            if len(heap) < 3:
                heapq.heappush(heap, i)
            else:
                heapq.heappushpop(heap, i)
        return heap[0] if len(heap) == 3 else max(heap)