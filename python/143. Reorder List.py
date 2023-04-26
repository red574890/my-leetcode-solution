
0/5
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tmp = []
        first = head
        while first != None:
            tmp.append(first.val)
            first = first.next
        

        first = head
        start = 0
        end = len(tmp)-1

        while start <= end:

            if(start == end):
                first.val = tmp[start]
            else:

                first.val = tmp[start]

                first = first.next

                first.val = tmp[end]

                first = first.next
            
            start += 1 
            end -= 1
