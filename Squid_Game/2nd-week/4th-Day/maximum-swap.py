class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = []
        s = defaultdict(list)
        for idx, n in enumerate(str(num)):
            s[n] = idx
            arr.append(n)
        
        sorted_nums = sorted(arr, reverse=True)

        largest = -1
        min_id = -1                       
        for i in range(len(arr)):
            if sorted_nums[i] != arr[i]:                
                largest = sorted_nums[i]
                min_id = i
                break
                            
        if largest == min_id:
            return num
        
        max_idx = s[largest]       
        arr[max_idx], arr[min_id] =  arr[min_id] , arr[max_idx]
        
        return int(''.join(arr))