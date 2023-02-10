class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        dct=defaultdict(int)
        lst=[(k, l) for k in range(n) for l in range(n) if img2[k][l]]
        for i in range(n):
            for j in range(n):
                if  img1[i][j]:
                    for k, l in lst:
                        dct[(i-k, j-l)]+=1
        return len(dct) and max(dct.values())