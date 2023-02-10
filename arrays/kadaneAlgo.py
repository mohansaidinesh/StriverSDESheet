class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res,s = nums[0],nums[0]
        for i in range(1,len(nums)):
            s = max(nums[i],s+nums[i])
            res = max(s,res)
        return res
