class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sets = []
        n = len(scores)
        dp = [0] * n
        for i in range(len(scores)):
            sets.append([ages[i],scores[i]])
        sets.sort()
        sets.reverse()
        maxim = 0 
        for i in range(n): 
            for j in range(i,-1,-1): 
                if sets[i][1] <= sets[j][1]: 
                    dp[i] = max(dp[i], dp[j]+sets[i][1]) 
            maxim = max(maxim, dp[i])  
        return maxim  