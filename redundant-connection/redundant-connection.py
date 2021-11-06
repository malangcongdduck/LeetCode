class Solution(object):
    def findRedundantConnection(self, edges):
        global matrix
        global visited
        global size 
        size = len(edges) + 1
        matrix=[[0]*size for _ in range(len(edges)+1)]
        
        #하나씩 edge를 추가하면서 cycle 검사 (뒤에서 부터 추가)
        for i in range(size-1):
            edge = edges[i]
            matrix[edge[0]][edge[1]] = 1
            matrix[edge[1]][edge[0]] = 1
            visited = [0] * size
            if self.has_cycle(edge[0], -1):
                return edge
        
    def has_cycle(self, u, pre):
        global matrix
        global visited
        global size 
        if visited[u] == 0:
            visited[u] = 1
            for v in range(size):
                if matrix[u][v] == 1 and v!= pre:
                    if self.has_cycle(v, u):
                        return True
            visited[u] = 0
            return False
        else:
            return True
                
