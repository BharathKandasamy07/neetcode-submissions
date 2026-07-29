class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        i = 1
        j = 0
        res = 0
        while i < n:
            if nums[i] > nums[j]:
                while i < n - 1 and nums[i] < nums[i + 1]:
                    i += 1
                res = max(res, i - j + 1)
                j = i
            elif nums[i] < nums[j]:
                while i < n - 1 and nums[i] > nums[i + 1]:
                    i += 1
                res = max(res, i - j + 1)
                j = i
            else:
                res = max(res, i - j)
                while i < n - 1 and nums[i] == nums[i + 1]:
                    i += 1
                if i == n - 1:
                    return res
                j = i
            i += 1
        return max(res, i - j + 1)
