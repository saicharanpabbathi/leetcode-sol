/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    struct ListNode *p1;
    
    while(node->next!=NULL)
    {
        p1=node;
        node->val=node->next->val;
        node=node->next;        
    }
    p1->next=NULL;
    
}