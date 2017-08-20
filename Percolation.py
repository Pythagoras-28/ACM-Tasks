import random
from math import sqrt
def initializeGrid(n,grid):
    for x in range(sqr):
        grid[x]=[x,False,1]#[root,isOpen,size]
    grid[-1]=[-1,True,1]
    grid[sqr]=[sqr,True,1]
def openSite(num):
    if grid[num][1]==False:
        grid[num][1]=True
        return 1
        #numOpen+=1
    else :
        return 0
def isOpen(n):
    return grid[n][1]
def root(n,grid):
        while(n!=grid[n][0]):
            grid[n][0]=grid[grid[n][0]][0]
            n=grid[n][0]
        return n

def quickUnion(p,q,grid):
        i=root(p,grid)
        j=root(q,grid)
        if(i==j):
            return
        if (grid[i][2]<grid[j][2]):
            grid[i][0]=j
            grid[j][2]+=grid[i][2]
        else:
            grid[j][0]=i
            grid[i][2]+=grid[j][2]
if __name__ == "__main__":
    n,t=map(int,raw_input().split())
    sqr=n*n
    pVals=[]
    for test in range(t):
        grid={}
        numOpen=0
        initializeGrid(n,grid)
        while True:
            rand=random.randrange(0,sqr)

            numOpen+=openSite(rand)
            if isOpen(rand+1):
                quickUnion(rand,rand+1,grid)
            if isOpen(rand-1):
                quickUnion(rand,rand-1,grid)
            if isOpen(max(-1,rand-n)):
                quickUnion(rand,max(-1,rand-n),grid)
            if isOpen(min(sqr,rand+n)):
                quickUnion(rand,min(sqr,rand+n),grid)

            if root(-1,grid)==root(sqr,grid):#checks for percolation
                pVals.append(numOpen)
                #print numOpen
                break
    mean=float(sum(pVals))/(float(t)*float(sqr))
    print 'Mean= ', mean
    total=0
    for val in pVals:
        total+=(float(val)/float(sqr)-mean)**2
    stdev=sqrt(float(total)/float(t-1))
    print "Std Dev= ",stdev
    interval=[mean-(1.96*stdev)/sqrt(t),mean+(1.96*stdev)/sqrt(t)]
    print """95% confidence interval """,interval
