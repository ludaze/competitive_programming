class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def solve(start, k):
            
            if (start, k) in memo:
                return memo[(start, k)]
            
            if start == n or n - start <= k:
                return 0
            
            ans = sys.maxsize
            count = defaultdict(int)
            most_freq = 0
            
            for j in range(start, n):
                c = s[j]
                count[c] += 1
                most_freq = max(most_freq, count[c])
                
                comp_len = 1 + (len(str(most_freq)) if most_freq > 1 else 0)
                
                prev = (j - start + 1 - most_freq)
                if  k >= prev:
                    ans = min(ans, comp_len + solve(j+1, k - prev))
            
            memo[(start, k)] = ans
            
            return ans
        
        
        n = len(s)
        memo = {}
        
        return solve(0, k)