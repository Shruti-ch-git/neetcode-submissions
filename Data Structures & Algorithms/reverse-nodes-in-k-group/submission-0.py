class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Find the kth node from groupPrev
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            # Reverse the group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Reconnect
            temp = groupPrev.next   # old head becomes tail after reversal
            groupPrev.next = kth
            groupPrev = temp
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        p=k
        prev=None
        curr=head
        while True:
            while p>0:
                if dummy.next != None :
                    dummy=dummy.next
                    p-=1
                else:
                    False
            p=k
            while curr!= dummy:
                temp=curr.next
                curr.next=prev
                prev = curr
                curr=temp
            prev.next=dummy
            
 """           
            


        
 
        