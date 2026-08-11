class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complement = {'(' : ')', '{': '}', '[': ']'}
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if not stack or complement[stack.pop()] != i:
                    return False
        return not stack

