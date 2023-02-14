class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        for ch in s:
            if ch == "b":
                b += 1
                        
        best = b
        curr = b
        for ch in s:
            if ch == "b":
                curr -= 1
            else:
                curr += 1
            best = max(best, curr)
        
        return len(s) - best

        return total