class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def aps (nums,k):
            if k==0:
                return 0
            d={}
            for i in nums:
                d[i]=0
            j=diff=ans=0
            for i in range(len(nums)):
                d[nums[i]]+=1
                if d[nums[i]]==1:
                    diff+=1
                if diff<=k:
                    ans+=(i-j+1)
                if diff > k:
                    while k < diff and j < i :
                        d[nums[j]]-=1
                        if d[nums[j]]==0:
                            diff-=1
                        j+=1
                    ans+=(i-j+1)
            return ans
        return aps(nums,k)-aps(nums,k-1)