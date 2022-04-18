# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        hd,tl = None,None
        l1 = list1
        l2 = list2
        while l1 != None and l2 != None :
            m = min(l1.val,l2.val)
            if hd == None:
                hd = ListNode(m)
            elif tl == None:
                tl = ListNode(m)
                hd.next = tl
            else:
                temp = ListNode(m)
                tl.next = temp
                tl = temp
            if l1.val == m:
                l1 = l1.next
            else:
                l2 = l2.next

        while l1 != None :
            m = l1.val
            if hd == None:
                hd = ListNode(m)
            elif tl == None:
                tl = ListNode(m)
                hd.next = tl
            else:
                temp = ListNode(m)
                tl.next = temp
                tl = temp
            l1 = l1.next

        while l2 != None :
            m = l2.val
            if hd == None:
                hd = ListNode(m)
            elif tl == None:
                tl = ListNode(m)
                hd.next = tl
            else:
                temp = ListNode(m)
                tl.next = temp
                tl = temp
            l2 = l2.next
        return hd