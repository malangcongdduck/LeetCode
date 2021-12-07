class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        self.res = set()
        self.visit=[0]*len(tiles)
        

        def dfs(seq, idx):
            
            if len(seq) == idx:
                self.res.add(seq)
                return
            
            for i in range(len(tiles)):
                if self.visit[i] == 0:
                    self.visit[i] = 1
                    dfs(seq+tiles[i], idx)
                    self.visit[i] = 0
        
        for i in range(1, len(tiles)+1):
            dfs('', i)

        
        print(self.res)
        return len(self.res)
            
            
