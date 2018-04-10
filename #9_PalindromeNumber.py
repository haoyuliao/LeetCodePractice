def reverse(self, x):
    s = (x>0)-(x<0)
    r = int(str(s*x)[::-1])
    return bool((x-s*r == 0)*(r<2**31))
print(reverse("ss", -2147447412))

