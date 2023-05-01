# stack
# O(n)


class Solution(object):
    def isValid(self, s):
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for p in s:
            if stack and pair.get(stack[-1]) == p:
                stack.pop()
            else:
                stack.append(p)

        return False if stack else True

class Solution(object):
    def isValid(self, s):
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for p in s:
            if stack and pair[stack[-1]] == p:
                stack.pop()
            else:
                stack.append(p)

        return False if stack else True
    

# 가지치기를 하자
class Solution(object):
    def isValid(self, s):
        pair = {')': '(', '}': '{', ']': '['}
        stack = []
        for p in s:
            if p in pair:
                if stack and stack.pop() == pair[p]:
                    pass
                else: return False
            else:
                stack.append(p)

        return not stack


s = Solution()
s.isValid('()[]{}')