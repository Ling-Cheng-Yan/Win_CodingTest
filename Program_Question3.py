class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        dummy=ListNode()    # Create a dummy Node
        tail=dummy
        
        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next     # Move pointer of dummyNode
        
        if l1:   # If some elemnts of l1 still exists, then add them at the end of new linked list
            tail.next=l1
        elif l2:
            tail.next=l2
            
        return dummy.next