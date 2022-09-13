# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        mergedHead = None
        if list1.val < list2.val:
            mergedHead = list1
            list1 = list1.next
        else:
            mergedHead = list2
            list2 = list2.next
        
        mergedTail = mergedHead
        
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
            
            mergedTail.next = temp
            mergedTail = temp
        
        if list1:
            mergedTail.next = list1
        elif list2:
            mergedTail.next = list2
        
        return mergedHead
        
        