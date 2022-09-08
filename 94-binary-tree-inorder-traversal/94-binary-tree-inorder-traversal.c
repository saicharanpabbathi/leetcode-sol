/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int t=0;
void inorder(struct TreeNode *h,int *a)
{
    if(h==NULL)
        return;
    inorder(h->left,a);
    a[t]=h->val;
    t++;
    inorder(h->right,a);
    
}
int* inorderTraversal(struct TreeNode* root, int* returnSize){
    int *a;
    t=0;
    a=(int*)malloc(201*2);
    inorder(root,a);
    *returnSize=t;
    return a;
    

}