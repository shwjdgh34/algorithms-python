class Solution(object):
    def countBinarySubstrings(self, s):
        prev_b = -1
        stack = []
        for b in s:
            if prev_b != b:
                stack.append(1)
            else:
                stack[-1] += 1
            prev_b = b
                
        total = 0
        for i in range(0,len(stack)-1):
            total = total + min(stack[i],stack[i+1])
            
        return total

s = Solution()
s.countBinarySubstrings("00110011")