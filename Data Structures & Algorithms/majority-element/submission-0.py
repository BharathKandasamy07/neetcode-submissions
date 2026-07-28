class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        max_ele = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                max_ele = nums[i]
                count += 1
            elif nums[i] != max_ele:
                count -= 1
            else:
                count += 1
        return max_ele
