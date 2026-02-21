# Definition for singly-linked list node is usually provided as:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # Start at the head of the list
        curr = head
        
        # Traverse until the end of the list
        while curr and curr.next:
            # If the current node's value equals the next node's value
            if curr.val == curr.next.val:
                # Skip the next node by pointing current to the one after it
                curr.next = curr.next.next
            else:
                # If they are different, just move forward
                curr = curr.next
                
        # Return the original head, which now points to a unique list
        return head

