def reverse(self, x):
    if x == 0:
        return True
    s = (x>0)-(x<0)
    r = int(str(s*x)[::-1])
    return bool((x-r == 0)*(r<2**31)*s)
print(reverse("ss", 0))

