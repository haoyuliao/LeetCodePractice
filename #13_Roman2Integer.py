class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        R2Int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        n = len(s)-1
        c = 0
        for i in range(n, -1, -1):
            if i <  n and i+1 != c and R2Int[s[i]] < R2Int[s[i+1]]:
                c = i
                ans = ans - R2Int[s[i]]
            else:
                ans = ans + R2Int[s[i]]
        return ans
    
print(Solution.romanToInt("S","MMMDCCCLXXXVIII")) #3888
