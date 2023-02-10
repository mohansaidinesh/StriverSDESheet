class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for i in nums:
            counts[i] += 1
        i = 0
        for k in range(3):
            while counts[k] > 0:
                nums[i] = k
                counts[k] -= 1
                i += 1
