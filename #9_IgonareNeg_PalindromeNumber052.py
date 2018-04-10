def reverse(self, x):
    #return str(x) == str(x)[::-1] #Extra space.
    if x < 0: return False
    ans = 0
    num = x
    while num > 0:
        ans = ans*10 + num%10
        num =  num//10
    
    return ans == x

print(reverse("ss", 10))

