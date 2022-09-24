# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def kk(h,k,s,l1,l2):
    if(h==None):
        return l1
    elif(h.left==None and h.right==None and s+h.val==k):
        l2.append(h.val)
        l1.append(l2[:])
        l2.pop()
        return l1
    else:
        l2.append(h.val)
        kk(h.left,k,s+h.val,l1,l2)
        kk(h.right,k,s+h.val,l1,l2)
        l2.pop()
        return l1
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return kk(root,targetSum,0,[],[])
        