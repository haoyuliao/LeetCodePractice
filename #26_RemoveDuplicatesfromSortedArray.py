class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums = sorted(nums)
        n = 0
        r = 0
        rn = 0
        for i in  range(0, len(nums)):
            if r != nums[i]:
                n += 1
                r = nums[i]
                nums[i-rn:i] = nums[i]
                rn = 0
            else:
                rn += 1
        return n
    
    def removeDuplicates11(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]
        print(A)
        return newTail + 1

arr = [1,1,1,2,2,3,3,3]

print(Solution.removeDuplicates11("ss",arr))

#for i in arr:
    #print(i)
