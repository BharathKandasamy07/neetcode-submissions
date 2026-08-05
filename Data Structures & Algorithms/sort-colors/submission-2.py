class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        for k in nums:
            if k == 1:
                j += 1
            elif k == 0:
                i += 1
                j += 1
        
        k = 0
        while k < i:
            nums[k] = 0
            k += 1
        while k < j:
            nums[k] = 1
            k += 1
        while k < len(nums):
            nums[k] = 2
            k += 1
        return nums