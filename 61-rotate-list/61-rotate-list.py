# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        temp = head
        prev = None
        length = 0
        while temp:
            temp=temp.next
            length+=1
        if k%length==0:
            return head
        else:
            k = k%length
        temp = head
        while k:
            while temp:
                if temp.next.next is None:
                    prev = temp.next
                    temp.next = None
                temp = temp.next
            prev.next = head
            head = prev
            temp = head
            k-=1
        return head
        
        