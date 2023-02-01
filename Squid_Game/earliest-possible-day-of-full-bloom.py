class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        maxHeap = list(zip([-grow for grow in growTime], plantTime))
        heapify(maxHeap)
        plantTime, ans = 0, 0
        while maxHeap:
            grow, plant = heappop(maxHeap)
            plantTime += plant
            ans = max(ans, plantTime - grow)
        return ans