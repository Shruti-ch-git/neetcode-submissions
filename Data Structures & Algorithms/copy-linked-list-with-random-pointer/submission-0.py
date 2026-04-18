
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None  # Edge case: Empty list

        # Step 1: Create new nodes and interweave them within the original list
        cur = head
        while cur:
            new_node = Node(cur.val)  # Create a copy
            new_node.next = cur.next  # Connect new node to the next original node
            cur.next = new_node       # Place the copied node after the original
            cur = new_node.next       # Move to the next original node

        # Step 2: Assign `random` pointers to the copied nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next  # Assign the copied random pointer
            cur = cur.next.next  # Skip the copied node, move to the next original node

        # Step 3: Separate the copied list from the original list
        cur = head
        new_head = head.next
        copy_cur = new_head

        while cur:
            cur.next = cur.next.next  # Restore original list
            if copy_cur.next:
                copy_cur.next = copy_cur.next.next  # Move copied list forward
            cur = cur.next
            copy_cur = copy_cur.next

        return new_head  # Return the head of the copied list
