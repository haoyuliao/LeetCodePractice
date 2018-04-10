class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x)/2147483648 > 1:
            return 0
        
        rx = int(str(x)[::-1]) if str(x)[::-1][-1] != "-" else int(str(x)[::-1][-1]+str(x)[::-1][:-1])
        
        return 0 if abs(rx)/2147483648 > 1 else rx

print(Solution.reverse("s",int(1563847412)))
