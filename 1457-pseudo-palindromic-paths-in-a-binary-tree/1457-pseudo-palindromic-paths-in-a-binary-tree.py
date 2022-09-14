# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def palin(h,l,a):
    l[h.val-1]+=1
    if h.left==None and h.right==None:
        c=0
        for i in l:
            if i&1==1:
                c+=1
        if c==1 or c==0:
            l[h.val-1]-=1
            return a+1
    if h.left!=None:
        a=palin(h.left,l,a)
    if h.right!=None:
        a=palin(h.right,l,a)
    l[h.val-1]-=1
    return a
    
    
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        l=[0 for i in range(9)]
        return palin(root,l,0)
        