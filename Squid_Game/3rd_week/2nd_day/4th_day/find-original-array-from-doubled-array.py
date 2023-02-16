class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 :
            return []
        changed.sort()
        arr = []
       
        counts = defaultdict(int)
        for i in changed:
            counts[i] += 1
       
        ind = len(changed)-1
        while ind >= 0:
            
            num = changed[ind]
          
            if counts[num] == 0:
             
                ind -= 1
            elif num % 2 != 0:
          
                return []
            else: # 
                
                counts[num] -= 1
                counts[num//2] -=1 
                ind -= 1
                arr.append(num//2)
        
        if len(arr) == len(changed)//2:
            return (arr)
        else:
            return []