import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        self.idx = []
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                self.idx.append(i)
                
        return random.choice(self.idx)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)