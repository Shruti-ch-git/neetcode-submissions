# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = t = ListNode()
        while list1 and list2 :
            if list1.val<list2.val:
                t.next=list1
                list1=list1.next
            else:
                t.next=list2
                list2=list2.next
            t=t.next
        t.next= list1 or list2 #imp step
        return dummy.next
#dummy: Remains stationary at the very beginning of the list. It acts as a permanent anchor so you can easily return the final list using dummy.next.t (often called curr or tail): This is your "active" pointer. As you build or traverse the list, you move t forward (e.g., t = t.next), but dummy stays put

        