# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # Create last place in the queue
        prev = None
        # Create the new end of the line by taking the former first place
        curr = head

        while curr:
            # Use nxt to keep track of who was next in line per the old order
            nxt = curr.next
            # Have the latest in line point to the thing behind them
            curr.next = prev
            # The person we were just looking at is now behind us
            prev = curr
            # We move our current view to the person that was next in line
            curr = nxt
        
        # Return the line?
        return prev
