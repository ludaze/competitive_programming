class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if n % 2 == 0:
            for i in range(1,(n//2)+1):
                arr.append(i)
                arr.append(-i)
        else:
            arr = []
            for j in range(1,(n//2)+1):
                arr.append(j)
                arr.append(-j)
            arr.append(0)
        return arr