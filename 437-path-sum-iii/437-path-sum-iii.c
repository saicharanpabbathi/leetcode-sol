/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int count(struct TreeNode* root,int ans,long long int s,int k);
int path(struct TreeNode *root,int ans,int k);
int path(struct TreeNode *root,int ans,int k)
{
    if(root==NULL)
        return ans;
    ans=count(root,ans,0,k);
    if(root->left!=NULL)
        ans=path(root->left,ans,k);
    if(root->right!=NULL)
        ans=path(root->right,ans,k);
    return ans;      
    
}
int count(struct TreeNode* root,int ans,long long int s,int k)
{
    if(k==s+root->val)
    {
        ans++;
    }
    if(root->left!=NULL&&root->right!=NULL)
    {
        ans=count(root->left,ans,s+root->val,k);
        ans=count(root->right,ans,s+root->val,k);
    }
    else if(root->left!=NULL)
    {
        ans=count(root->left,ans,s+root->val,k);
    }
    else if(root->right!=NULL)
    {
        ans=count(root->right,ans,s+root->val,k);
    }
    return ans;
}
int pathSum(struct TreeNode* root, int targetSum){
    int a=0;
    return path(root,0,targetSum);
    
    

}