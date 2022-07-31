# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        ln = len(lst)
        lst1 = lst[:ln//2]
        lst2 = lst[math.ceil(ln/2):]
        lst2 = lst2[::-1]
        if lst1 == lst2:
            return True
        return False