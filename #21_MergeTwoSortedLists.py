class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#[1,2,4]
L1 = ListNode(1)
L1.next = ListNode(2)
L1.next.next = ListNode(4)
#[1,3,4]
L2 = ListNode(1)
L2.next = ListNode(3)
L2.next.next = ListNode(4)
#[5,6,7]
L3 = ListNode(4)
L3.next = ListNode(5)
L3.next.next = ListNode(6)

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        arr = []
        while l1:
            arr.append(l1.val)
            l1 = l1.next
        while l2:
            arr.append(l2.val)
            l2 = l2.next
        arr = sorted(arr)
        
        sortNode = ListNode(None)
        curNode = sortNode
        pre = None
        for i in arr:
            curNode.val = i
            curNode.next = ListNode(None)
            pre = curNode
            curNode = curNode.next
            
        if curNode.next == None:
            pre.next = None

        return sortNode
    
def mergeTwoListsOther(a, b):#From StefanPochmann
    if a and b:
        if a.val > b.val:
            a, b = b, a
        a.next = mergeTwoListsOther(a.next, b)
    return a or b


a = mergeTwoListsOther(L3, L1)
c = a
while c:
    print(c.val)
    c = c.next

