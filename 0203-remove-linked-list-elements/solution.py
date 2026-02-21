# Definition for singly-linked list node is usually provided as:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head, val):
        # Create a dummy node pointing to the head
        # This makes it easy to delete the actual head if needed
        dummy = ListNode(0)
        dummy.next = head
        
        # 'curr' will traverse the list
        curr = dummy
        
        while curr.next:
            if curr.next.val == val:
                # Skip the node by linking current to the one after next
                curr.next = curr.next.next
            else:
                # Only move forward if we didn't delete a node
                curr = curr.next
        
        # Return the new head (skipping our dummy node)
        return dummy.next

