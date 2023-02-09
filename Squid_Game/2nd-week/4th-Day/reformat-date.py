class Solution:
    def reformatDate(self, date: str) -> str:
        ans = ""
        nums = set(["0","1","2","3","4","5","6","7","8","9"])
        dates = date.split(" ")
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        ans += (dates[2] + "-")
        if (months.index(dates[1])+1) < 10:
            ans += "0"
            ans += (str(months.index(dates[1])+1) + "-")
        else:
            ans += (str(months.index(dates[1])+1) + "-")

        if dates[0][1] in nums:
            ans += dates[0][0]
            ans += dates[0][1]
        else:
            ans += "0"
            ans += dates[0][0]

        return ans