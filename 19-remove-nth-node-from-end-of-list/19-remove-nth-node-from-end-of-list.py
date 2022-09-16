# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        count = 0
        while dummy:
            count+=1
            dummy = dummy.next
        if count == n:
            return head.next
        dummy = head
        for i in range(count - n -1):
            dummy = dummy.next
        
        dummy.next = dummy.next.next
        return head
            
        