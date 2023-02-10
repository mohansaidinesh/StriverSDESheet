class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=j=n-1
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        if i>0:
            while nums[j]<=nums[i-1]:
                j-=1
            nums[j],nums[i-1]=nums[i-1],nums[j]
        nums[i:]=nums[i:][::-1]
