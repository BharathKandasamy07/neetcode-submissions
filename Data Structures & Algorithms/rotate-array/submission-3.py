class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for j in range(k):
            temp = nums[0]
            for i in range(1, n):
                temp, nums[i] = nums[i], temp
            nums[0] = temp
        return nums