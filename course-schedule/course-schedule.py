class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.visited = [0] * numCourses
        self.checked = [0] * numCourses
        self.G = [[0] * numCourses for _ in range(numCourses)]
        
        for i in range(len(prerequisites)):
            self.G[prerequisites[i][0]][prerequisites[i][1]]=1
            
        for i in range(numCourses):
            if self.check_cycle(numCourses, i):
                return False
        return True
    
    def check_cycle(self, size, n):
        if self.visited[n] == 0:
            if self.checked[n] == 1:
                return False
            self.checked[n] = 1
            self.visited[n] = 1

            for i in range(size):
                if self.G[n][i] == 1:
                    if self.check_cycle(size, i):
                        return True
            self.visited[n] = 0
            return False
        else:
            return True
    
        