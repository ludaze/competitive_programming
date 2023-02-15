class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber>0:
            letters = (columnNumber-1) % 26
            ans += chr(letters + 65)
            columnNumber = (columnNumber-1) // 26
        return ans[::-1]
        