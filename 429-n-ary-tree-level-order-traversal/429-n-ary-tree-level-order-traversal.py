"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
def level(h,lev,le,l):
    if h==None:
        return le
    if lev<le:
        l[lev].append(h.val)
    else:
        l1=[h.val,]
        le+=1
        l.append(l1)
        
    for i in h.children:
        le=level(i,lev+1,le,l)
    return le
    
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        l=[]
        level(root,0,0,l)
        return l
        