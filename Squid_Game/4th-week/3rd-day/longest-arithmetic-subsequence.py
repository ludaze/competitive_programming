class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
    
        if len(nums) == 2:
            return 2
		
        ad = {}  
        count = 0
      
        for i in range(len(nums)):
            ad[i] = {}
        
        diff = nums[len(nums) - 2] - nums[len(nums) - 1]
        ad[len(nums) - 2][diff] = 2
        ad[len(nums) - 1][0] = 1
        
        for i in range(len(nums) - 3, -1, -1):
            for j in range(i+1, len(nums)):
    
                diff = nums[i] - nums[j]
                
                if diff in ad[j]:
                    if diff in ad[i]:
                        ad[i][diff] = max(ad[j][diff] + 1, ad[i][diff])
                    else:
                        ad[i][diff] = ad[j][diff] + 1
                    count = max(count, ad[i][diff])
                else:
                    if diff not in ad[i]:
                        ad[i][diff] = 2
                    else:
                        ad[i][diff] = max(ad[i][diff], 2)
                    count = max(count, ad[i][diff])
       
        return count