from functools import reduce 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot_pdt = 1
        flag_0 = False
        for i in nums:
            if i == 0 and not flag_0:
                flag_0 = True
                continue
            elif i == 0:
                return [0] * len(nums)
            tot_pdt *= i
        res = []
        if flag_0:
            for i in nums:
                res.append(tot_pdt if i == 0 else 0)
        else:
            for i in nums:
                res.append(tot_pdt // i)
        
        return res