class Solution(object):
    def generateParenthesis(self, n):
        def dfs(r, n):
            if r == 0 and n == 0:
                return [""]
            rArray = []
            if n > 0 : 
                def add_left_parenthesis(n):
                    return "(" + n

                temp = dfs(r+1, n-1)
                rArray += list(map(add_left_parenthesis,temp))
                    
            if r > 0 :
                def add_right_parenthesis(n):
                    return ")" + n

                temp = dfs(r-1, n)
                rArray += list(map(add_right_parenthesis,temp))

            return rArray 

        return dfs(0,n)

s = Solution()
print(s.generateParenthesis(3))
