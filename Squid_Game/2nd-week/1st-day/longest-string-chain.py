class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def predecessor(word1, word2):
            if len(word2) - len(word1) != 1:
                return False
            dist = 0
            i = j = 0
            while i < len(word1):
                if word1[i] != word2[j]:
                    if dist:
                        return False
                    dist = 1
                    j += 1
                else:
                    i += 1
                    j += 1
            return True
                    
        words = sorted(words,key=lambda x:len(x))
        dp = [1]*len(words)
        for i in range(len(words)):
            for j in range(i):
                if predecessor(words[j],words[i]):
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)