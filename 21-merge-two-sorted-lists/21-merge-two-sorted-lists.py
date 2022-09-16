# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        temp = result
        while list1 is None and list2 is None:
            return result.next
        
        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            temp.next = node
            temp = temp.next
        
        while list1:
            node = ListNode(list1.val)
            temp.next = node
            temp = temp.next
            list1 = list1.next
        
        while list2:
            node = ListNode(list2.val)
            temp.next = node
            temp = temp.next
            list2 = list2.next
        return result.next
                
        
        