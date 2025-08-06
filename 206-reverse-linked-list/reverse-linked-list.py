# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rev = None 
        prev = head 
        if not head:
            return rev    
        cur = head.next
        if not cur:
            return head
        while cur:
            rev = cur
            cur = cur.next 
            rev.next = prev

            prev = rev
        head.next = None
        return rev
            
            


            


        