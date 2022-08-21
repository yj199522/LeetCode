# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        temp = result
        carry = 0
        
        while l1 is not None and l2 is not None:
            total = l1.val + l2.val + carry
            carry = total//10
            total = total%10
            node = ListNode(total)
            temp.next = node
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            total = l1.val + carry
            carry = total//10
            total = total%10
            node = ListNode(total)
            temp.next = node
            temp = temp.next
            l1 = l1.next
        
        while l2 is not None:
            total = l2.val + carry
            carry = total//10
            total = total%10
            node = ListNode(total)
            temp.next = node
            temp = temp.next
            l2 = l2.next
        
        if carry:
            node = ListNode(carry)
            temp.next = node
            temp = temp.next
        
        return result.next