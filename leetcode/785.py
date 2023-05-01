class Solution(object):
    # dfs
    def isBipartite(self, graph):
        n = len(graph)
        bipartite = [-1]*n
        isBipartite = True

        def dfs(self, b, v):
            if not isBipartite:
                    return
            for next_v in graph[v]:
                if bipartite[next_v] == -1:
                    bipartite[next_v] = 1 - b
                    dfs(bipartite[next_v], next_v)    
                elif bipartite[next_v] != 1-b:
                    isBipartite = False
                    
        for edges in graph:
            for v in edges:
                if bipartite[v] == -1:
                    bipartite[v] = 0
                    dfs(0, v)
                
        return isBipartite

        
     
            

