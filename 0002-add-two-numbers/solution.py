# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Continue as long as there is a node to process or a carry left over
        while l1 or l2 or carry:
            # Get values from nodes, or 0 if the list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10
            
            # Update result list
            curr.next = ListNode(new_digit)
            curr = curr.next
            
            # Move to next nodes in input lists
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next

