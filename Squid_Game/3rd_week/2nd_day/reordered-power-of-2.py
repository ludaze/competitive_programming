class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num=str(n)
        counter=collections.Counter(num)
        lst=[]
        for i in range(0,99):
            s='1'+'0'*i
            m=int(s,2)
            if m>10**9:
                break
            lst.append(str(m))
        for i in lst:
            if len(i)!=len(num):
                continue
            counter2=collections.Counter(i)
            if counter == counter2:
                return True
        return False