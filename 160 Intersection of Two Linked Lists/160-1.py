# time m+n, space m or n

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp = set()
        while(headA != None):
            temp.add(headA)
            headA = headA.next
        while(headB != None):
            if(headB in temp):
                break
            headB = headB.next
        if(headB):
            return headB
        else:
            return