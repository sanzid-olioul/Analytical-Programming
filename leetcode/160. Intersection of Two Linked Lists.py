# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        itr1,itr2 = headA,headB
        while itr1:
            s.add(itr1)
            itr1 = itr1.next
        while itr2:
            if itr2 in s:
                return itr2
            itr2 = itr2.next
        return None
