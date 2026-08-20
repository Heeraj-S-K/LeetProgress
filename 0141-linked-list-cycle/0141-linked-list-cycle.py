# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         # self.val = x
#         # self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Check for empty list or single isolated node
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        # Traverse until fast pointer reaches the end
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # If pointers meet, a cycle exists
            if slow == fast:
                return True
                
        # If fast reaches null, there is no cycle
        return False
