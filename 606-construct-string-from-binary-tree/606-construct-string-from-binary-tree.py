# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def st(h,s):
    if h==None:
        return s
    s=st(h.left,s+str(h.val)+"(")
    if s[-1]=="(" and h.right==None:
        return s[:len(s)-1]
    s+=")"
    if h.right==None:
        return s
    s=st(h.right,s+"(")
    return s+")"

        
        
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return st(root,"")
        