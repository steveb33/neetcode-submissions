# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Handle the edges first
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1

        # Realias because i don't know why not??
        l1 = list1
        l2 = list2

        # handle which one to start with
        if l1.val < l2.val:
            merge = l1
            first = l1
            l1 = l1.next
        else:
            merge = l2
            first = l2
            l2 = l2.next

        # Loop through the lists until one is empty
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                merge.next = l1
                l1 = l1.next
            else:
                merge.next = l2
                l2 = l2.next    
            merge = merge.next
        
        # Once one or the other lists are depleted, we pin the remaineder
        if l1 == None:
            merge.next = l2
    
        if l2 == None:
            merge.next = l1
            
        return first