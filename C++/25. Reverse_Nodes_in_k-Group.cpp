  /**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *current=head;

        if(k==1){
            return head;
        }
    
        ListNode *dummy = new ListNode(-1);
        ListNode *previous = dummy;
        dummy->next = head;
        for(int i=1;current;i++){
            if(i%k==0){
                previous=reverse(previous,current->next);
                current = previous->next;
                
            }else{
                current=current->next;
            }
            
        }
        return dummy->next;
       
    }
private:
    ListNode *reverse(ListNode *preNode, ListNode *nxtNode){
        ListNode *cur=preNode->next, *nxt=NULL,*last = preNode->next,*pre = NULL;
        
        while(cur!=nxtNode){
            nxt=cur->next;  
            cur->next=pre;
            pre=cur;
            cur=nxt;
              
        }
        
        preNode->next = pre;
        last->next = nxtNode;
        
        return last;
        
}
};
