# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       head = ListNode(0)
       curr = head
       while (list1 != None or list2 != None):
           
           if(list1 == None):
               curr.next = list2
               curr = curr.next
               list2 = list2.next
               continue
           elif(list2 == None):
               curr.next = list1
               curr = curr.next
               list1 = list1.next
               continue
               
           else:
               if(list1.val <= list2.val):
                   curr.next = list1
                   curr = curr.next
                   list1 = list1.next
               else:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next

       head = head.next
       return head
         
