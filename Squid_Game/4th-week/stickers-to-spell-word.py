class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        n = len(stickers)
        stickers = [Counter(sticker) for sticker in stickers]
        
        @lru_cache(None)
        def dp(s):
            if s=='':
                return 0
            cs = Counter(s)
            ans = float('inf')

            for sticker in stickers:
                if s[0] not in sticker:
                    continue
                ans = min(ans,1+dp(''.join(ch*ct for ch,ct in sorted((cs-sticker).items()))))
            return ans
            
        val =  dp(''.join(sorted(target)))
        return -1 if val==float('inf') else val