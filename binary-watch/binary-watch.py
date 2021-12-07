class Solution(object):
    def readBinaryWatch(self, turnedOn):
        
        self.res = []
        led = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        
        # how many digits are still on 
        def dfs(h, m, idx, n):
            if h > 11 or m > 59:
                return
            if n == 0:
                self.res.append("{:d}:{:02d}".format(h, m))
                return
            for i in range(idx, len(led)):
                if i <= 3:
                    dfs(h + led[i], m, i + 1, n - 1)
                elif i < len(led):
                    dfs(h, m + led[i], i + 1, n - 1)
                
            
        dfs(0, 0, 0, turnedOn)
        return self.res