import re

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(re.findall(s[0], s)) == len(s):
            return s
        oddMax = s[0]
        evenMax = s[0]
        #For odd number.
        for i in range(len(s)-2):
            if s[i:i+3] == s[i:i+3][::-1]:
                n = 1
                while 1:
                    if s[i-n:i+3+n] == s[i-n:i+3+n][::-1] and len(s[i-n:i+3+n])%2 == 1 and len(s[i-n:i+3+n])>3:
                        n += 1
                    else:
                        n -= 1
                        if len(s[i-n:i+3+n]) > len(oddMax):
                            oddMax = s[i-n:i+3+n]
                        break      
        #For even number.
        for i in range(len(s)-1):
            if s[i:i+2] == s[i:i+2][::-1]:
                n = 0
                while 1:
                    if s[i-n:i+2+n] == s[i-n:i+2+n][::-1] and len(s[i-n:i+2+n])%2 == 0 and len(s[i-n:i+2+n]) > 1:
                        n += 1
                    else:
                        n -= 1
                        if len(s[i-n:i+2+n]) > len(evenMax):
                            evenMax = s[i-n:i+2+n]
                        break
        return oddMax if len(oddMax)>len(evenMax) else evenMax
