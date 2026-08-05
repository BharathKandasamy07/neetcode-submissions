class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n < 2:
            return nums
        
        left_part = nums[:n // 2]
        right_part = nums[n // 2:]

        left_part = self.sortArray(left_part)
        right_part = self.sortArray(right_part)

        m = len(left_part)
        p = len(right_part)
        i, j = 0, 0
        sorted_array = []
        while i < m and j < p:
            if left_part[i] < right_part[j]:
                sorted_array.append(left_part[i])
                i += 1
            else:
                sorted_array.append(right_part[j])
                j += 1
        
        if i == m:
            sorted_array.extend(right_part[j:])
        else:
            sorted_array.extend(left_part[i:])
        
        return sorted_array


        