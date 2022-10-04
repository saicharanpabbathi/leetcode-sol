/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool hasPathSum(struct TreeNode* root, int targetSum){
    if(root==NULL)
        return false;
    if(targetSum-root->val==0&&root->left==NULL&&root->right==NULL)
        return true;
    else
    {
        if(hasPathSum(root->left,targetSum-root->val)||hasPathSum(root->right,targetSum-root->val))
            return true;
        else
            return false;
    }

}