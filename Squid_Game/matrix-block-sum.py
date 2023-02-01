class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        new=[row[::] for row in mat]
        row=[[0 for y in range(len(mat[0]))] for x in range(len(mat))]

        for x in range(len(mat)):
            for y in range(len(mat[0])):
                row[x][y] += mat[x][y]
                if y+1 < len(mat[0]):
                    row[x][y+1] += row[x][y]
        
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                lower,upper,left,right = max(0,x-k), min(len(mat)-1,x+k), max(0,y-k), min(len(mat[0])-1,y+k)
                new[x][y]-=mat[x][y];     
                for u in range(lower,upper+1):
                    if left==0:
                        new[x][y] += row[u][right]
                    else:
                        new[x][y] += row[u][right]-row[u][left-1]
        return new
