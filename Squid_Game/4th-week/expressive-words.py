class Solution:
    def helper(self,word,target):
        l1,l2= 0,0
        r1,r2 = 0,0
        
        while l1 < len(word) and l2<len(target):
            if word[l1] != target[l2]:
                return 0
            while r1<len(word) and word[l1]==word[r1]:
                    r1+=1
            len1 = r1-l1
            while r2<len(target) and target[l2]==target[r2]:
                    r2+=1
            len2 = r2-l2
            if len1 > len2:
                return 0
            if len1 != len2 and len2 < 3:
                return 0
            l1,l2 = r1,r2
        if l1==len(word) and l2==len(target):
            return 1    
        return 0
     
    def expressiveWords(self, target: str, words: List[str]) -> int:
        output = 0
        for word in words:
            output += self.helper(word,target)
        return output