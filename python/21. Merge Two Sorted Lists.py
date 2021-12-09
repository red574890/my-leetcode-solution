# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new=[]

        while(list1!=None or list2!=None):
            
            if(list1==None and list2!=None):
                new.append(list2.val)
                list2=list2.next
            
            elif(list1!=None and list2==None):
                new.append(list1.val)
                list1=list1.next
            
            else:
                if(list1.val>list2.val):
                    new.append(list2.val)
                    list2=list2.next
                else:
                    new.append(list1.val)
                    list1=list1.next

        for i in range(len(new)):
            if(i==0):
                first=ListNode(new[len(new)-i-1],None)
            else:
                first=ListNode(new[len(new)-i-1],first)
        
        if(len(new)==0):
            return None
    
        return first
            
            
            
        
