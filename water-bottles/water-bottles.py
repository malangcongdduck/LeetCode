class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        count = 0 #마신 개수
        temp = 0 #갱신되는 빈병 개수
        
        while True:
                       
            #병 비우기
            for i in range(numBottles):
                count += 1
                temp += 1
            
            if temp / numExchange > 0:
                numBottles = temp / numExchange
                temp = temp % numExchange
            else:
                return count
            
            
                