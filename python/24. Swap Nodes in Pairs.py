# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        res = head
        while(head!= None):
            if(n==0):
                first = head
                first_val = head.val
                n=1
            elif(n==1):
                second = head
                second_val = head.val
                first.val = second_val
                second.val = first_val
                n=0
            head = head.next
            
        return res
