class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicts = {}
        list1 = []
        for i in range(len(s)):
            if s[i] in dicts:
                if dicts[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                dicts[s[i]] = t[i]
                if (t[i]) in list1:
                    return False
                list1.append(t[i])
        return True