# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s , f = head, head
        while f and f.next:
            s= s.next
            f= f.next.next

        curr , prev = s.next, None
        s.next= None
        while curr:
            temp= curr.next
            curr.next = prev
            prev = curr
            curr = temp


        l1 = head
        l2= prev
        while l2:
            t1, t2 = l1.next, l2.next
            l1.next= l2
            l2.next= t1
            l1,l2= t1,t2
        