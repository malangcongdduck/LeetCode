class Solution(object):
    result = []
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.selected =[0]*len(nums)
        
        for i in range(len(nums)+1):
            self.temp = []
            self.explore(i, nums, 0, self.selected)
            self.result = self.result + self.temp
            #print('result: ',self.result)
        
        return self.result
        
    def explore(self, ii, nums, start, selected):
        if ii == 0:
            num = []
            for i in range(len(selected)):
                if selected[i] == 1:
                    num.append(nums[i])
                    
            self.temp.append(num)
            print('temp: ',self.temp)
            return
            
        for i in range(start, len(selected)):
            if selected[i] == 0:
                selected[i] = 1
                self.explore(ii-1, nums, i+1, selected)
                selected[i] = 0
        return
        