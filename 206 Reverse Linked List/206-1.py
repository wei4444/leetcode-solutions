# iterative
# time n, space 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create(self, vals):
        now = self
        for i in range(len(vals)-1):
            now.val = vals[i]
            now.next = ListNode()
            now = now.next
        now.val = vals[-1]

    def output(self):
        now = self
        r = ''
        while(now != None):
            r += str(now.val)
            now = now.next
        print(r)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        now = head
        pre = None
        while(now != None):
            nex = now.next
            now.next = pre
            pre = now
            now = nex
        
        return pre

n = ListNode()
n.create([1,2,3,4,5])
n.output()
n2 = Solution().reverseList(n)
n2.output()