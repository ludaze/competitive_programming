class Solution:
    def numberOfWays(self, s: str) -> int:
        cnt = 0
        if s[0] == "1":
            start = [[0,1]]
        else:
            start = [[1,0]]
        if s[-1] == "1":
            end = [[0,1]]
        else:
            end = [[1,0]]
        for i in range(1,len(s)):
            if s[i] == "1":
                start.append([start[-1][0],start[-1][1]+1])
            else:
                start.append([start[-1][0]+1,start[-1][1]])
        for j in range(len(s)-2,-1,-1):
            if s[j] == "1":
                end.append([end[-1][0],end[-1][1]+1])
            else:
                end.append([end[-1][0]+1,end[-1][1]])
        end.reverse()
        for i in range(1,len(s)-1):
            if s[i] == "1":
                if (start[i-1][0] > 0) and (end[i+1][0] > 0):
                    cnt += start[i-1][0] * end[i][0]
            else:
                if (start[i-1][1] > 0) and (end[i+1][1] > 0):
                    cnt += start[i-1][1] * end[i][1]
        return cnt