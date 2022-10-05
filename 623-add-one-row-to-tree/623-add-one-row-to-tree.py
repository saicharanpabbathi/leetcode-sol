# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def arow(root,val,d):
    if root==None:
        return root
    if d==1:
        l1=TreeNode(val,root.left,None)
        r1=TreeNode(val,None,root.right)
        root.left=l1
        root.right=r1
        return root
    arow(root.left,val,d-1)
    arow(root.right,val,d-1)
    return root
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            t=TreeNode(val,root,None)
            return t
        else:
            return arow(root,val,depth-1)
        
        