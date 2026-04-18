# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N=0
        cur = head
        while cur:
            N+=1
            cur = cur.next

        i1 = N-n
        if i1==0:
            head = head.next

        else:
            cur = head
            for i in range (N-1):
                if(i+1)== i1:
                    cur.next = cur.next.next
                    break
                else:
                    cur = cur.next
        return head

        