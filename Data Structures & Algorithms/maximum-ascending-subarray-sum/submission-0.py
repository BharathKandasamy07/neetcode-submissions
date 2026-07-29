class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        is_ascending = False
        curSum = 0
        res = 0
        for i in range(n - 1):
            curSum += nums[i]
            if nums[i] < nums[i + 1]:
                is_ascending = True
            else:
                is_ascending = False
                res = max(curSum, res)
                curSum = 0
        curSum +=  (nums[-1] if is_ascending else 0)
        return max(res, curSum)
