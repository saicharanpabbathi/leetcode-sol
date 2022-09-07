# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def pru(h):
    if h==None:
        return 0
    l=pru(h.left)
    if l==0:
        h.left=None
    r=pru(h.right)
    if r==0:
        h.right=None
    if h.val==1:
        return l+r+1
    return l+r
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if pru(root)>0:
            return root
        else:
            return None
        