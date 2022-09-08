def island(gr,l,f,r1,c1,r,c,l1):
    if len(l1)<=f-1:
        l1.append(1)
    else:
        l1[f-1]+=1
    l[r1][c1]=f
    if(r1>=1 and gr[r1-1][c1]==1 and l[r1-1][c1]==0):
        island(gr,l,f,r1-1,c1,r,c,l1)
    if(r1<r-1 and gr[r1+1][c1]==1 and l[r1+1][c1]==0):
        island(gr,l,f,r1+1,c1,r,c,l1)
    if(c1>=1 and gr[r1][c1-1]==1 and l[r1][c1-1]==0):
        island(gr,l,f,r1,c1-1,r,c,l1)
    if(c1<c-1 and gr[r1][c1+1]==1 and l[r1][c1+1]==0):
        island(gr,l,f,r1,c1+1,r,c,l1)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        l=[]
        l2=[]
        for i in grid:
            l1=[0 for x in grid[0]]
            l.append(l1)
        i=0
        r=len(grid)
        c=len(grid[0])
        for j in range(r):
            for k in range(c):
                if(l[j][k]==0 and grid[j][k]==1):
                    i+=1
                    island(grid,l,i,j,k,r,c,l2)
        if len(l2)==0:
            return 0
        else:
            return max(l2)
        
        