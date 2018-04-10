class Solution:
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        LCP = ""
        x = ""
        for i in range(n):
            if len(strs[i]) == 0:
                return strs[i]
            if i != n-1:
                x += "strs["+str(i)+"][j] =="
            else:
                x += "strs["+str(i)+"][j]"
                
        j = 0
        while 1:
            try:
                if eval(x):
                    LCP = strs[0][0:j+1]
                    j +=1
                else:
                   return LCP
            except:
                return LCP
    ##From jason.xxr
    def longestCommonPrefix2(self, strs):
        prefix = '';
        # * is the unpacking operator, essential here
        for z in zip(*strs):
            bag = set(z);
            if len(bag) == 1:
                prefix += bag.pop();
            else:
                break;
        return prefix;
print(Solution.longestCommonPrefix2("str", ["leet", "leetscode", "leet", "leeds"]))
#print(Solution.longestCommonPrefix("str", ["", "leetscode", "leet", "leeds"]))
#print(Solution.longestCommonPrefix("str", ["leet", "leetscode", "leet", ""]))
#print(Solution.longestCommonPrefix("str", [" ",""]))
