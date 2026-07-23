class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        j = 0
        res = 0
        while i < len(nums):
            if nums[i] == 1:
                j = i
                while i < len(nums) and nums[i] == 1:
                    i += 1
                res = max(res, i - j)
            i += 1
        return res