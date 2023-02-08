class Solution:
    
    def __init__(self):
        self.visited = set()
        
    def dfs(self, src, dest, adj):
        if src == dest and adj[src]:
            return 1.0
        
        self.visited.add(src)
        
        for n, v in adj[src]:
            if n in self.visited:
                continue
            productWeight = self.dfs(n, dest, adj)
            if productWeight != -1:
                return productWeight * v
            
            
        return -1            
            
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        adj = defaultdict(set)
        for i in range(len(equations)):
            adj[equations[i][0]].add((equations[i][1],values[i]))
            adj[equations[i][1]].add((equations[i][0],1.0/values[i])) 
        
        output = []
        
        for i in queries:
            output.append(self.dfs(i[0], i[1], adj))
            self.visited = set()
        
        return output