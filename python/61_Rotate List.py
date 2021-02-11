# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(head==None):
            return None
        elif(head.next==None):
            return head
        else:
            #length test
            currt=head
            length=1
            while(currt.next!=None):
                    currt=currt.next
                    length+=1
            k=k%length
       
            
            n=0
            while(n<k):
                curr=head
                while(curr.next.next!=None):
                    curr=curr.next
                curr.next.next=head
                head=curr.next
                curr.next=None
                n+=1
            return head
        
