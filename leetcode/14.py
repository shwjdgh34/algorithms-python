# 단순 brute force
# O(n^2)

class Solution(object):
    def longestCommonPrefix(self, strs):
        common_prix = ""
        min_len = len(min(strs))
        str_nums = len(strs)

        for i in range(min_len):
            flag = True
            for j in range(1, str_nums):
                if  strs[0][i] != strs[j][i]:
                    flag = False
                    break
            
            if not flag:
                break
            
            common_prix += strs[0][i]

        return common_prix
                
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix= ''
        num = len(strs)
        print(*strs)
        print(zip(*strs))
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix += x[0]
            else:
                break
        return prefix       


s = Solution()
print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))