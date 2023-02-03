
    def pickIndex(self) -> int:
        n = randint(0, self.prefix[-1]-1)
        left, right = 0, len(self.prefix)-1
        while left < right:
            mid = (left+right+1)//2
            if self.prefix[mid] <= n:
                left = mid
            else:
                right = mid-1

        return left