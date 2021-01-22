class Solution:
    def rob(self, nums: List[int]) -> int:
        ans=[0 for _ in range(len(nums))]
        
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            ans[0]=nums[0]
        elif len(nums)==2:
            ans[0]=nums[0]
            ans[1]=max(nums[0],nums[1])
        elif len(nums)>=3:
            ans[0]=nums[0]
            ans[1]=max(nums[0],nums[1])
                
            for i in range(2,len(nums)):
                ans[i]=max(ans[i-1],ans[i-2]+nums[i])
        
        return ans[len(nums)-1]