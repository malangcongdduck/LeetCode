class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        global visited
        visited=[0]*len(rooms)
        self.visit(0, rooms)

        for i in visited:
            if i == 0:
                return False
        return True
                    
    def visit(self, key, rooms):
        global visited
        visited[key] = 1
        for i in rooms[key]:
            if visited[i] == 0:
                self.visit(i, rooms)