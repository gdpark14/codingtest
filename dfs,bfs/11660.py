import sys
import collections

n,m=map(int,sys.stdin.readline().split())

board=[]
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    board.append(temp)

sum_board=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        sum_board[i][j]=sum_board[i-1][j]+board[i-1][j-1]

for i in range(1,n+1):
    for j in range(1,n+1):
        sum_board[i][j]=sum_board[i][j-1]+sum_board[i][j]

for i in range(m):
    y1,x1,y2,x2=map(int,sys.stdin.readline().split())
    print(sum_board[y2][x2]-sum_board[y2][x1-1]-sum_board[y1-1][x2]+sum_board[y1-1][x1-1])
