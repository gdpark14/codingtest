import sys
import collections
sys.setrecursionlimit(10000)

def dfs(i,j):

    if i<0 or i>=sero or j<0 or j>=garo:
        return False
    if baechu[i][j]==1:
        baechu[i][j]=0

        dfs(i,j-1)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i+1,j)

        return True
    else:
        return False

testcase=int(input())

for case in range(testcase):
    garo,sero,baechu_num=map(int,sys.stdin.readline().split())
    baechu=[[0]*garo for _ in range(sero)]

    index=[]
    for _ in range(baechu_num):
        a,b=map(int,sys.stdin.readline().split())
        baechu[b][a]=1
        index.append([b,a])
    ans=0

    for temp_index in index:
        if dfs(temp_index[0],temp_index[1])==True:
            ans+=1
    print(ans)



