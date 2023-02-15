class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def isPerfectSquare(n): 
            return int(n ** 0.5) == n ** 0.5
        
        @lru_cache(None)
        def check(nums, length, tol=2):
            count = 0
            for i in range(length - 1):
                if not isPerfectSquare(nums[i] + nums[i + 1]): count += 1
                if count == tol: return False
            return True
        
        n, seen, ans, q = len(nums), set(), set(), deque([((nums[0],), 1)])
        while q:
            cur, i = q.popleft()
            if i == n:
                if check(cur, i, 1): ans.add(cur)
                continue
            for p in (cur[:j] + (nums[i],) + cur[j:] for j in range(i + 1)):
                if p not in seen and check(p, i + 1): 
                    seen.add(p) 
                    q.append((p, i + 1))

        return len(ans) 