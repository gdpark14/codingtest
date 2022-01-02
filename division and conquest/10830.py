import sys
import collections

length,how_many=map(int,sys.stdin.readline().split())

matrix=[list(map(int,sys.stdin.readline().split())) for _ in range(length)]

def multiplication(left,right):
    matrix=[]
    n=len(left)
    ans=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j]+=left[i][k]*right[k][j]
            ans[i][j]=ans[i][j]%1000
    return ans
def identity(n):
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        temp[i][i]=1
    return temp

def matmul(what,index):
    if index==2:
        return multiplication(what,what)
    elif index==1:
        length=len(what)
        identity_matrix=identity(length)
        return multiplication(what,identity_matrix)
    elif index%2==0:
        next_index=index//2
        left=matmul(what,next_index)
        right=left
        return multiplication(left,left)
    else:
        left=matmul(what,index-1)
        right=what
        return multiplication(left,right)

result=matmul(matrix,how_many)

n=len(result)
for i in range(n):
    for j in range(n):
        if j==n-1:
            print(result[i][j])
        else:
            print(result[i][j],end=' ')
