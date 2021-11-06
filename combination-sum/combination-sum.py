class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global result
        result =[]
        
        for i in range(len(candidates)):
            self.explore(candidates, target, [], 0)
        
        result = set(list(map(tuple,result)))
        return set(result)
        
    def explore(self, candidates, gozero, li, start):
        if gozero == 0:
            result.append(li)
            return
        elif gozero < 0:
            return
        
        for i in range(start, len(candidates)):
                self.explore(candidates, gozero-candidates[i], li + [candidates[i]], i)