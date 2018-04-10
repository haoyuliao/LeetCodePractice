def reverse(self, x):
    s = (x>0)-(x<0)
    r = int(str(s*x)[::-1])
    return s*r*(r<2**31)
print(reverse("ss", 0))

