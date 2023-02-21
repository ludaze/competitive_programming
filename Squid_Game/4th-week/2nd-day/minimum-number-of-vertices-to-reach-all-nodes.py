class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = []
        for i in range(n):
            graph.append([])
        
        for [i,j] in edges:
            graph[j].append(i)

        res = []
        for i in range(n):
            if not graph[i]:
                res.append(i)
        
        return res