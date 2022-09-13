/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
int ans=INT_MIN;
int kk(TreeNode *r);
int kk(TreeNode *r)
{
    int l,ri;
    if(r==NULL)
        return 0;
    l=kk(r->left);
    ri=kk(r->right);
    ans=max(ans,l+ri+r->val);
    return max(0,max(l,ri)+r->val);
    
}
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        ans=INT_MIN;
        kk(root);
        return ans;
        
    }
};