# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        temp = result
        if head is None or head.next is None:
            return head
        
        while head:
            if head.next:
                node = ListNode(head.next.val)
                temp.next = node
                temp = temp.next
                node = ListNode(head.val)
                temp.next = node
                temp = temp.next
                head = head.next.next
            else:
                node = ListNode(head.val)
                temp.next = node
                temp = temp.next
                head = head.next
        return result.next
        