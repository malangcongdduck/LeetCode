class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        li = []
        for i in range(n+1):
            b=str(bin(i))
            b_count=b.count('1')
            li.append(b_count)
            
        return li