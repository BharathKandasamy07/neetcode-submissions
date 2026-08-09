from typing import List


class Solution:

  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
      current_sum = numbers[left] + numbers[right]

      if current_sum == target:
        return [left + 1, right + 1]  # 1-indexed result
      elif current_sum > target:
        right -= 1  # Sum is too large; reduce the larger number
      else:
        left += 1  # Sum is too small; increase the smaller number

    return []