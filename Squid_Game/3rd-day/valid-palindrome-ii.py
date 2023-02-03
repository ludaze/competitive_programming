class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s)-1
        str1 =''
        str2=''
        while p1<p2:
            if s[p1] != s[p2]:
                str1 = s[:p1]+s[p1+1:]
                str2 = s[:p2] + s[p2 +1:]
                
                break
            p1 = p1+1
            p2 = p2-1
        if str1 == str1[::-1] or str2 == str2[::-1]:
            return True