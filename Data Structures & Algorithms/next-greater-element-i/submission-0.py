class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ele_map = defaultdict(lambda : -1)
        stack = []
        for i in nums2:
            if not stack or stack[-1] > i:
                stack.append(i)
            else:
                while stack and stack[-1] < i:
                    ele_map[stack.pop()] = i
                stack.append(i)
        
        res = []
        for i in nums1:
            res.append(ele_map[i])
        
        return res
