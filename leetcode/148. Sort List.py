# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp = head
#         tail = None
#         while (temp!= tail and tail != None) or (temp and tail==None):
#             ano = head
#             while (ano != tail and tail != None) or (ano and tail==None):
#                 if ano.next:
#                     if ano.val > ano.next.val:
#                         ano.val , ano.next.val = ano.next.val , ano.val
#                 ano = ano.next
#             tail =ano
#             temp= temp.next
        
#         return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        lst = []
        while cur:
            lst.append(cur.val)
            cur = cur.next
        lst = sorted(lst)

        cur = head
        i=0
        while cur:
            cur.val = lst[i]
            i+=1
            cur = cur.next
        return head
