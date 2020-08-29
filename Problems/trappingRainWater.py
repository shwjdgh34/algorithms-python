'''
stack 이용한 풀이
O(n^2)
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        answer = 0
        stack = []
        trapped = height[:]
        popElement = (0, 0)
        for i, h in enumerate(height):
            while stack and h >= stack[-1][1]:
                popElement = stack.pop()

            if stack:
                for j in range(stack[-1][0]+1, i):
                    trapped[j] = h
            else:
                for j in range(popElement[0], i):
                    trapped[j] = popElement[1]
            stack.append((i, h))

        zip_object = zip(trapped, height)

        for water, wall in zip_object:
            diff = water - wall
            answer += diff

        return answer


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
