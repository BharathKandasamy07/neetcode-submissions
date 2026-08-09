class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        j = 0
        i = 0
        while i < len(nums):
            if nums[i] not in seen:
                nums[j] = nums[i]
                j += 1
                seen.add(nums[i])
            i += 1
        return j

