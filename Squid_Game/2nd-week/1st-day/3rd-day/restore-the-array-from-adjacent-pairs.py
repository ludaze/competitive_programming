class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dicts = defaultdict(list)
        
        for adj in adjacentPairs:
            dicts[adj[0]].append(adj[1])
            dicts[adj[1]].append(adj[0])
        
        def find_first(dic) -> int:
            for i in dic:
                if len(dic[i]) == 1:
                    return i
        
        first = find_first(dicts)
        res = [first]
        visited = {first}
        stack = [dicts[first]]
        while stack:
            cur = stack.pop()
            for adj in cur:
                if adj not in visited:
                    stack.append(dicts[adj])
                    visited.add(adj)
                    res.append(adj)
        return res
        