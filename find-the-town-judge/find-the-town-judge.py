class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        town = [[0] * n for _ in range(n)]
        judge = -1
        for i in trust:
            town[i[0]-1][i[1]-1] = 1
        
        for i in range(n):
            count = 0
            for j in range(n):
                if town[i][j] == 0:
                    count+=1
            if count == n:
                judge = i
                break
        if judge == -1:
            return judge
        else:
            count = 0
            for i in range(n): 
                if town[i][judge] == 1:
                    count += 1
            if count == n-1:
                return judge+1
            else:
                return -1
        
        