/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* h, int n){
    struct ListNode *p,*p1;
    int i=0;
    p=h;
    p1=h;
    while(i<n)
    {
        p1=p1->next;
        i++;
    }
    while(p1!=NULL&&p1->next!=NULL)
    {
        p=p->next;
        p1=p1->next;
    }
    if(p==h&&p1==NULL)
        return p->next;
    else
    {
        p->next=p->next->next;
    }
    return h;
    

}