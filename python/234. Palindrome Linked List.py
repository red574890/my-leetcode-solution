# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        while head != None:
            tmp.append(head.val)
            head = head.next

        

        start = 0
        end = len(tmp) - 1


        while start < end:
            if(tmp[start]!=tmp[end]):
                return False

            start+= 1
            end -= 1

        return True

