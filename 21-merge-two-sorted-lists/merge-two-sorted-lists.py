# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = list1
        temp2 = list2
        new_head = ListNode()
        curr = new_head

        while temp and temp2:
            if temp.val > temp2.val:
                curr.next = temp2
                temp2 = temp2.next
            else:
                curr.next = temp
                temp = temp.next
            curr = curr.next
        if temp:
            curr.next = temp
        else:
            curr.next = temp2
        return new_head.next
                


        