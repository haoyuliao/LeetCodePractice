class Solution(object):
    def removeElementV1(self, nums, val):
        n=0
        s=0
        for i in range(len(nums)-n):
            if nums[i]==val:
                s=i
                n+=1
            if n>0 and nums[i] != val:
                nums[s-n+1] = nums[i]
                nums[i] = val
                s = i
        return nums
    def removeElementV2(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start +=1
        return nums



#print(Solution.removeElementV2("test",[0,1,2,2,3,0,4,2], 2))
#print(Solution.removeElementV2("test",[0,1,2,3,2,0,2,4,2], 2))
#print(Solution.removeElementV2("test",[0,1,2,3,0,4,2,2,2,2,2,2], 2))
#print(Solution.removeElementV2("test",[0,1,2,2,3,0,2,4,2], 2))

print(Solution.removeElementV2("test",[0,1,2,2,3,0,4,2], 2))
print(Solution.removeElementV2("test",[0,1,2,3,2,0,2,4,2], 2))
print(Solution.removeElementV2("test",[0,1,2,3,0,4,2,2,2,2,2,2], 2))
print(Solution.removeElementV2("test",[0,1,2,2,3,0,2,4,2], 2))
