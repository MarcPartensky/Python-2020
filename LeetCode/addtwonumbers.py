
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(2)

class Solution:
    @staticmethod
    def pack(n):
        if len(n)>0:
            l = ListNode(int(n[-1]))
            l.next = Solution.pack(n[:-1])
            return l
    @staticmethod
    def unpack(l):
        if l.next is not None:
            return [l.val]+Solution.unpack(l.next)
        else:
            return [l.val]
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = Solution.unpack(l1)
        l2 = Solution.unpack(l2)
        n = str(int("".join([*map(str, reversed(l1))]))+int("".join([*map(str, reversed(l2))])))
        return Solution.pack(n)

s = Solution()
l = s.addTwoNumbers(l1, l2)
print(Solution.unpack(l))
