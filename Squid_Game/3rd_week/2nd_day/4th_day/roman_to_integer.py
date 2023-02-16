class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range(len(s)):
            sum += nums[s[i]]
            if i != len(s)-1 and nums[s[i]] <  nums[s[i + 1]]:
                sum = sum - nums[s[i]] - nums[s[i]]
        return sum