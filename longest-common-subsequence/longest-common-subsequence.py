class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        memo=[[0] * 1001 for _ in range(1001)]
        
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i][j-1], memo[i-1][j])

                    
        return memo[len(text2)-1][len(text1)-1]