class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        memo = [[0] * 10001 for _ in range(101)]
    
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
                    
        if memo[len(s)][len(t)] == len(s):
            return True
        else:
            return False