def island(gr,l,f,r1,c1,r,c):
    l[r1][c1]=f
    if(r1>=1 and gr[r1-1][c1]=="1" and l[r1-1][c1]==0):
        island(gr,l,f,r1-1,c1,r,c)
    if(r1<r-1 and gr[r1+1][c1]=="1" and l[r1+1][c1]==0):
        island(gr,l,f,r1+1,c1,r,c)
    if(c1>=1 and gr[r1][c1-1]=="1" and l[r1][c1-1]==0):
        island(gr,l,f,r1,c1-1,r,c)
    if(c1<c-1 and gr[r1][c1+1]=="1" and l[r1][c1+1]==0):
        island(gr,l,f,r1,c1+1,r,c)
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        l=[]
        for i in grid:
            l1=[0 for x in grid[0]]
            l.append(l1)
        i=0
        r=len(grid)
        c=len(grid[0])
        for j in range(r):
            for k in range(c):
                if(l[j][k]==0 and grid[j][k]=="1"):
                    i+=1
                    island(grid,l,i,j,k,r,c)
        return i
                    
        
            
            
        