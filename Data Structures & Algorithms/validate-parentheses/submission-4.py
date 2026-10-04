class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '[': ']',
            '{': '}',
            '(': ')'
        }

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char != pairs[stack[-1]]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) > 0:
            return False

        return True
