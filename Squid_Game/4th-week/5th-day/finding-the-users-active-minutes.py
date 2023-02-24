class Solution:
   def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
    d={}
    for i in range(len(logs)):
        if logs[i][0] not in d:
            d[logs[i][0]]=[logs[i][1]]
        else:
            if logs[i][1] not in d[logs[i][0]]:
                d[logs[i][0]]+=[logs[i][1]]
    
    for i in d:
        d[i]=len(d[i])
    print(d)
    uam={}
    for i,j in d.items():
        if j not in uam:
            uam[j]=[j]
        else:
            uam[j]+=[j]
    for i in uam:
        uam[i]=len(uam[i])
    ans=[]
    for i in range(1,k+1):
        if i in uam:
            ans.append(uam[i])
        else:
            ans.append(0)
    return ans