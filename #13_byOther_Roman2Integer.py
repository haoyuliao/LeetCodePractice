import time

class Solution(object):
    """
    :type s: str
    :rtype: int
    """
    def romanToInt1(self, s):#Other
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res, i = 0, 0
        for i in range(len(s)):
            curr, nxt = s[i], s[i+1:i+2]
            if nxt and roman[curr] < roman[nxt]:
                res -= roman[curr]
            else:
                res += roman[curr]
        return res
    
    def romanToInt2(self, s):#Mine
        R2Int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        n = len(s)-1
        c = 0
        for i in range(n, -1, -1):
            if i <  n and i+1 != c and R2Int[s[i]] < R2Int[s[i+1]]:
                c = i
                ans -= R2Int[s[i]]
            else:
                ans += R2Int[s[i]]
        return ans
    
tStart = time.time()
for i in range(1000000):
    Solution.romanToInt1("S","MMMDCCCLXXXVIII") #3888
tEnd = time.time() 
print("--- %s seconds ---" % (tEnd- tStart ))

'''
tStart = time.time()
print(Solution.romanToInt1("S","MMMDCCCLXXXVIII")) #3888
tEnd = time.time() 
print("--- %s seconds ---" % (tEnd- tStart ))
'''


