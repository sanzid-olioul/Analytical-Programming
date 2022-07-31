# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def marge(lst,nd):
            if lst :
                if nd:
                    if lst.val > nd.val:
                        temp = ListNode(nd.val,lst)
                        lst= temp
                        nd = nd.next
                else:
                    return lst
            else:
                return nd
            nxt = lst.next
            while nd:
                if nxt and nxt.val < nd.val:
                    lst = lst.next
                    nxt = nxt.next
                else:
                    temp = ListNode(nd.val,lst.next)
                    lst.next = temp
                    nd = nd.next
            
            return lst
        if len(lists) ==0:
            return None
        elif len(lists)==2:
            return lists[0]
        val = None
        for i in range(len(lists)):
            val = marge(val,lists[i])
            
        return val

