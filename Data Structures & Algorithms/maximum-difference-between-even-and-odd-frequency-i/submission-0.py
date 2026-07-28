class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        odd_max = 0
        even_min = len(s)
        for i in counter.values():
            if i % 2 == 0 and i < even_min:
                even_min = i
            elif i % 2 != 0 and i > odd_max:
                odd_max = i
        return odd_max - even_min