class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lets = []
        digits = []
        heap = []
		
        for log in logs:
            res = log.split(' ')
            if res[1][0].isdigit():
                digits.append(log)
                continue
            cont = ' '.join(res[1:])
            iden = res[0]
            heapq.heappush(heap, (cont, iden)) 
        for _ in range(len(heap)):
            cont, iden = heapq.heappop(heap) 
            lets.append(iden + ' ' + cont)
    
        return lets + digits