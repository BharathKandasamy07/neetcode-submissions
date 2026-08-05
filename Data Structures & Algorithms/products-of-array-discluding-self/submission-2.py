from functools import reduce 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot_pdt = 1
        flag_0 = None
        for i in range(len(nums)):
            if nums[i] == 0 and flag_0 is None:
                flag_0 = i
                continue
            elif nums[i] == 0:
                return [0] * len(nums)

            tot_pdt *= nums[i]
        
        res = []
        if flag_0 is not None:
            res = [0] * len(nums)
            res[flag_0] = tot_pdt
            return res
        else:
            for i in nums:
                res.append(tot_pdt // i)
        
        return res